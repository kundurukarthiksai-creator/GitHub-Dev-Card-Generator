# GitHub Dev Card Generator Source

This folder contains the runnable app source.

Use the repository root README for the full project overview. The app source lives in:

```text
github-card-generator/
  backend/
  frontend/
  scripts/
  docker-compose.yml
```

Quick smoke test from this folder:

```powershell
cd github-card-generator
python -m venv .venv
.\.venv\Scripts\python -m pip install -r backend\requirements.txt
.\.venv\Scripts\python scripts\smoke-test.py
```

The backend can start without `GOOGLE_API_KEY`; when the key is missing, it uses deterministic fallback profile text instead of Gemini output.

