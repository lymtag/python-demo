# Claude Project Guide

## Project Intent

This repository contains a FastAPI web project for file-upload workflows, plus a
small backward-compatible CLI wrapper in `test2.py`.

## Collaboration Rules

- Read `AGENTS.md` first; it is the shared source of engineering standards.
- Keep production code simple and explicit.
- Do not perform live API calls while testing unless the user asks for an integration
  test.
- When adding behavior, add or update focused pytest cases in `tests/`.
- Put HTTP endpoints in `app/api/routes/`, shared logic in `app/services/`, and
  schemas in `app/schemas/`.
- Do not introduce additional framework-level abstractions unless repeated behavior
  makes the need obvious.

## Preferred Implementation Style

- Separate command-line orchestration from reusable functions.
- Keep FastAPI handlers thin.
- Make external services replaceable in tests.
- Favor small functions over inheritance-heavy designs.
- Use clear names and straightforward error handling.
