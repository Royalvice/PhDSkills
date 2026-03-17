# Environment

## Purpose

This skill should detect and repair its own Python environment before running validators or helper scripts.

## Baseline

- Python `3.10+`
- `pip`
- `PyYAML` for compatibility with `skill-creator/scripts/quick_validate.py`

## Health Check

Run:

```powershell
python scripts/check_python_env.py
```

If the report says `NOT READY`, bootstrap a dedicated environment:

```powershell
python scripts/bootstrap_python_env.py --venv-dir .venv
```

If `venv` creation fails, the bootstrap script automatically falls back to the current interpreter and installs only the missing packages there. This is important on some Miniconda builds where `ensurepip` is unavailable.

## Validation Path

When `.venv` exists, prefer:

```powershell
.\.venv\Scripts\python.exe C:\Users\lenovo\.codex\skills\.system\skill-creator\scripts\quick_validate.py .
```

If the bootstrap script falls back to the current interpreter, reuse the interpreter it prints at the end.

## Repair Policy

- Prefer creating or updating `.venv` instead of changing the global interpreter.
- If `.venv` is not possible, fall back explicitly instead of failing silently.
- Install only the packages actually needed by the workflow.
- If package installation fails because of network restrictions, request permission or escalate rather than silently skipping validation.
