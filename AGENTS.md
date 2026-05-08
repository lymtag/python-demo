# Project Agent Guide

## Scope

This project is a small FastAPI web application with a backward-compatible Python
upload CLI. Agents should keep changes narrow, testable, and compatible with both
HTTP and command-line usage.

## Working Standards

- Prefer dependency injection for external effects. Network calls should be easy to
  mock in tests.
- Keep FastAPI route handlers in `app/api/routes/`.
- Keep reusable behavior in `app/services/`.
- Keep CLI parsing in `test2.py` and reusable behavior out of the CLI wrapper.
- Use `pathlib.Path` for file-system paths.
- Raise clear Python exceptions for invalid local input, then let the CLI decide how
  to present output.
- Avoid hidden network calls in tests. Patch the boundary where `requests` is used.
- Keep secrets and environment-specific tokens out of new tests and docs.

## Design Pattern Baseline

- **Adapter boundary**: treat `requests.post` as an external adapter, isolated behind
  `app.services.upload_client.upload_file()`.
- **Functional core, imperative shell**: keep parsing, printing, and network I/O at
  the edge; keep response parsing and request preparation small and deterministic.
- **Layered web structure**: route handlers should orchestrate validation and
  responses; service modules should own business logic and external calls.
- **Single responsibility**: one function should either prepare/upload, parse a
  response, handle an HTTP route, or run the CLI flow.

## Test Standards

- Use `pytest`.
- Put tests under `tests/`.
- Use `tmp_path` for files and `monkeypatch` for external dependencies.
- Test success paths and local failure paths before adding integration tests.
- Command to run:

```bash
python3 -m pytest
```
