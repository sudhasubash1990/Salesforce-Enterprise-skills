"""Document converter interface."""

from __future__ import annotations

from abc import ABC, abstractmethod

from shared.models import ConversionJob, ConversionResult


class DocumentConverter(ABC):
    """Base class for all output format converters."""

    format_ext: str
    format_name: str

    @abstractmethod
    def convert(self, job: ConversionJob) -> None:
        """Write converted output to job.output_path."""

    def run(self, job: ConversionJob) -> ConversionResult:
        """Execute conversion and return structured result."""
        try:
            self.convert(job)
            return ConversionResult(
                source=job.rel_path,
                target=job.output_path.relative_to(job.root_path).as_posix(),
                format=self.format_name,
                status="success",
                converter=self.__class__.__name__,
            )
        except Exception as exc:  # noqa: BLE001
            return ConversionResult(
                source=job.rel_path,
                target=job.output_path.relative_to(job.root_path).as_posix(),
                format=self.format_name,
                status="failed",
                error=str(exc),
                converter=self.__class__.__name__,
            )
