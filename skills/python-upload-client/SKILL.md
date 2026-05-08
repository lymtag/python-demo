---
name: python-upload-client
description: Use when working on this Python FastAPI upload project, including upload behavior, CLI parsing, route handlers, response parsing, pytest tests, and project standards shared by OpenAI/Codex and Claude.
---

# Python Upload Web Project

## First Read

- Read `AGENTS.md` for shared OpenAI/Codex engineering standards.
- Read `CLAUDE.md` when preparing changes that should also work well in Claude
  Project context.
- Inspect `app/services/upload_client.py` before changing upload behavior.
- Inspect `test2.py` before changing CLI behavior.

## Workflow

1. Keep FastAPI routes in `app/api/routes/`.
2. Keep reusable behavior in `app/services/` and CLI orchestration in `test2.py`.
3. Treat outbound HTTP calls as an adapter boundary. Patch
   `app.services.upload_client.requests.post` in unit tests instead of making live
   network calls.
4. Use `pathlib.Path` for local files.
5. Preserve clear local validation errors, especially missing-file checks.
6. Add focused `pytest` cases under `tests/` for behavior changes.

## Design Pattern Baseline

- Use a functional-core, imperative-shell style.
- Keep route handlers thin and service modules deterministic where possible.
- Prefer small functions over classes until stateful behavior is truly needed.
- Keep external effects replaceable through narrow boundaries.
- Avoid extra framework abstractions unless duplication appears.

## Validation

Run:

```bash
python3 -m pytest
```
