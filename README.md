# OpsPilot AI

Security-aware AI cloud support ticket triage and workflow analytics. A portfolio prototype targeting AI cloud operations workflows.

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

## Design

- `app.py`: deterministic baseline logic; no external credentials or paid services needed.
- `tests/`: unit tests for security and correctness cases.
- Human review is required before any security remediation or operational action.
- Uses synthetic/example data only; no production cloud integration is claimed.

## AI extension roadmap

1. Add an optional LLM explanation adapter with schema validation and prompt-injection resistance.
2. Connect read-only cloud telemetry or ticket APIs with scoped credentials.
3. Build a FastAPI endpoint and TypeScript dashboard to collect user feedback and adoption metrics.
4. Add CI, structured logs, deployment documentation and measured before/after results.

## Responsible use

Treat model outputs as suggestions, not verified facts. Never place credentials or customer data in prompts.

## GitHub Pages demo

The static demo uses synthetic cases and embeds the Python results. Run `python demo_report.py` to reproduce the data. Preview by serving `docs` with `python -m http.server --directory docs`. In GitHub Pages, select **Deploy from a branch**, then **main** and **/docs**.
