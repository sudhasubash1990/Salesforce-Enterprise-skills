"""PDF converter via Word COM (docx intermediate) or Pandoc fallback."""

from __future__ import annotations

import os
import shutil
import tempfile
import time
from pathlib import Path

try:
    import pypandoc
except ImportError:
    pypandoc = None  # type: ignore

from converters.word_converter import WordConverter
from shared.converter_interface import DocumentConverter
from shared.file_utils import write_via_temp
from shared.markdown_parser import build_cover_md
from shared.models import ConversionJob


def _word_export_pdf(docx_path: Path, pdf_path: Path) -> None:
    """Convert DOCX to PDF using Microsoft Word COM automation."""
    import win32com.client

    word = win32com.client.DispatchEx("Word.Application")
    word.Visible = False
    word.DisplayAlerts = 0
    doc = None
    try:
        doc = word.Documents.Open(str(docx_path.resolve()), ReadOnly=True)
        doc.ExportAsFixedFormat(
            OutputFileName=str(pdf_path.resolve()),
            ExportFormat=17,
            OpenAfterExport=False,
            OptimizeFor=0,
            BitmapMissingFonts=True,
            DocStructureTags=True,
            CreateBookmarks=0,
            UseISO19005_1=False,
        )
    finally:
        if doc is not None:
            try:
                doc.Close(False)
            except Exception:  # noqa: BLE001
                pass
        try:
            word.Quit()
        except Exception:  # noqa: BLE001
            pass


class PDFConverter(DocumentConverter):
    format_ext = ".pdf"
    format_name = "pdf"

    def convert(self, job: ConversionJob) -> None:
        if pypandoc is None:
            raise RuntimeError("pypandoc is not installed")

        fd, temp_name = tempfile.mkstemp(suffix=".docx")
        os.close(fd)
        temp_docx = Path(temp_name)
        try:
            WordConverter().convert(
                ConversionJob(
                    source_path=job.source_path,
                    output_path=temp_docx,
                    root_path=job.root_path,
                    rel_path=job.rel_path,
                    format="docx",
                    meta=job.meta,
                    body=job.body,
                    config=job.config,
                )
            )

            fd2, temp_pdf_name = tempfile.mkstemp(suffix=".pdf")
            os.close(fd2)
            temp_pdf = Path(temp_pdf_name)
            try:
                last_err: Exception | None = None
                for _ in range(3):
                    try:
                        _word_export_pdf(temp_docx, temp_pdf)
                        if temp_pdf.exists() and temp_pdf.stat().st_size > 0:
                            write_via_temp(
                                job.output_path,
                                lambda target: target.write_bytes(temp_pdf.read_bytes()),
                            )
                            return
                    except Exception as exc:  # noqa: BLE001
                        last_err = exc
                        time.sleep(2)

                try:
                    from docx2pdf import convert as docx2pdf_convert

                    docx2pdf_convert(str(temp_docx), str(temp_pdf))
                    if temp_pdf.exists() and temp_pdf.stat().st_size > 0:
                        write_via_temp(
                            job.output_path,
                            lambda target: target.write_bytes(temp_pdf.read_bytes()),
                        )
                        return
                except Exception as exc:  # noqa: BLE001
                    last_err = exc

                content = job.body
                if job.config.get("generateCoverPage", True):
                    content = build_cover_md(job.meta) + job.body
                extra_args = ["--standalone"]
                if job.config.get("generateTOC", True):
                    extra_args.append("--toc")
                engines = ["wkhtmltopdf", "weasyprint", "xelatex", "pdflatex"]
                for engine in engines:
                    if engine == "wkhtmltopdf" and not shutil.which("wkhtmltopdf"):
                        continue
                    try:
                        pypandoc.convert_text(
                            content,
                            "pdf",
                            format="md",
                            outputfile=str(temp_pdf),
                            extra_args=extra_args + [f"--pdf-engine={engine}"],
                        )
                        if temp_pdf.exists() and temp_pdf.stat().st_size > 0:
                            write_via_temp(
                                job.output_path,
                                lambda target: target.write_bytes(temp_pdf.read_bytes()),
                            )
                            return
                    except Exception as exc:  # noqa: BLE001
                        last_err = exc
                raise RuntimeError(
                    f"PDF conversion failed. Install Microsoft Word or wkhtmltopdf. ({last_err})"
                )
            finally:
                if temp_pdf.exists():
                    try:
                        temp_pdf.unlink()
                    except OSError:
                        pass
        finally:
            for _ in range(5):
                try:
                    if temp_docx.exists():
                        temp_docx.unlink()
                    break
                except OSError:
                    time.sleep(1)
