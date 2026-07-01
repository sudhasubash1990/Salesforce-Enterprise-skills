# Enterprise Output Engine

Modular markdown-to-office conversion for the Salesforce Enterprise Skills platform.

## Features

- **Intelligent routing** — one format per artifact (`.docx`, `.pdf`, `.xlsx`, `.pptx`)
- **Pluggable converters** — `DocumentConverter` interface with dependency inversion
- **Generic rules** — `configuration/routing_rules.json` by `document_type` and filename
- **Project overrides** — `outputs/<project>/format-routing.json` for explicit routes
- **Auto-run** — agents convert after writing markdown to `outputs/`

## Installation

```powershell
pip install -r output-engine/requirements.txt
winget install --id JohnMacFarlane.Pandoc -e
```

**Windows PDF:** Microsoft Word recommended (uses Word COM via `win32com`). Close stray `WINWORD.EXE` processes if batch PDF conversion fails with file-lock errors.

## Usage

### Convert entire project folder

```powershell
python output-engine/convert.py --root outputs/utilities-digital-transformation --overwrite
```

### Convert single file (post-write hook)

```powershell
python output-engine/convert.py --file outputs/utilities-digital-transformation/03-requirements/brd.md
```

## Format Routing

| Artifact type | Format |
|---------------|--------|
| BRD, FRD, NFR | `.pdf` |
| Presentations | `.pptx` |
| Registers, RTM, stories, checklists | `.xlsx` |
| Narrative documents, plans, process maps | `.docx` |

## Architecture

```
output-engine/
├── orchestrator/     # OutputOrchestrator, Pipeline, ExecutionManager
├── configuration/    # Config loader, routing_rules.json
├── shared/           # Models, parser, converter interface
├── converters/       # Word, PDF, PPT, Excel
└── conversion_logging/  # conversion.log, conversion_report.json
```

## Agent Integration

After writing any file under `outputs/`, run:

```powershell
python output-engine/convert.py --file <path-to.md>
```

## Extension

1. Create a class implementing `DocumentConverter` in `converters/`
2. Register in `ExecutionManager._converters`
3. Add routing rule in `configuration/routing_rules.json`

## Legacy

`convert_markdown.py` is deprecated; use `convert.py`.
