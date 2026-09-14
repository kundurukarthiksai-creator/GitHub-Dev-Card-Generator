# GitHub Dev Card Generator

[![CI](https://github.com/kundurukarthiksai-creator/GitHub-Dev-Card-Generator/actions/workflows/ci.yml/badge.svg)](https://github.com/kundurukarthiksai-creator/GitHub-Dev-Card-Generator/actions/workflows/ci.yml)

Generate shareable developer identity cards from any public GitHub profile.

The app fetches GitHub profile/repository data, summarizes the developer profile, and renders a styled card that can be previewed in the browser. Gemini can be used for richer AI summaries when a key is configured; otherwise the backend falls back to deterministic profile text so the app can still run locally.

![GitHub Dev Card preview](./Screenshot%202026-05-17%20092339.png)

## What It Does

- Fetches public GitHub profile and repository data.
- Builds a developer card with avatar, bio, location, repository stats, top repositories, and common languages.
- Supports dark, light, and neon-style card themes.
- Uses Gemini for AI-generated profile analysis when `GOOGLE_API_KEY` is configured.
- Falls back to a deterministic summary when no Gemini key is available.
- Serves a static frontend and a FastAPI backend.

## Tech Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Python, FastAPI
- AI: Google Gemini API, optional
- Data: GitHub REST API
- Deployment: Docker / Docker Compose

## Project Layout

```text
github-dev-card-generator/
  github-card-generator/
    backend/
      main.py
      agent.py
      mcp_server.py
      requirements.txt
      .env.example
    frontend/
      index.html
      assets/
    scripts/
      smoke-test.py
    docker-compose.yml
```

## Local Setup

From the repository root:

```powershell
cd github-dev-card-generator\github-card-generator
python -m venv .venv
.\.venv\Scripts\python -m pip install -r backend\requirements.txt
Copy-Item backend\.env.example backend\.env
```

Optional environment variables in `backend\.env`:

```env
GOOGLE_API_KEY=
GITHUB_TOKEN=
```

`GOOGLE_API_KEY` enables Gemini-powered profile summaries. `GITHUB_TOKEN` is optional and only helps with GitHub API rate limits.

## Run

```powershell
.\.venv\Scripts\python -m uvicorn backend.main:app --host 0.0.0.0 --port 8080
```

Open:

```text
http://localhost:8080
```

## Smoke Test

```powershell
.\.venv\Scripts\python scripts\smoke-test.py
```

The smoke test checks:

- the FastAPI health function;
- backend import without `GOOGLE_API_KEY`;
- deterministic fallback profile analysis;
- card HTML generation.

## API

| Method | Endpoint | Purpose |
|---|---|---|
| `GET` | `/health` | Health check |
| `POST` | `/generate` | Generate a developer card |
| `GET` | `/card/{username}` | Retrieve a saved card |

Example request:

```json
{
  "username": "torvalds",
  "theme": "dark"
}
```

## Screenshots

| Dark | Light | Neon |
|---|---|---|
| ![](./Screenshot%202026-05-17%20092339.png) | ![](./Screenshot%202026-05-17%20092424.png) | ![](./Screenshot%202026-05-17%20092501.png) |

## Known Limitations

- Generated card HTML is local runtime output and is intentionally ignored by Git.
- Gemini output depends on external API availability and configured credentials.
- GitHub API calls may hit unauthenticated rate limits unless `GITHUB_TOKEN` is configured.
- The current frontend is static and intentionally lightweight.

## Status

This is a portfolio project cleanup pass. The backend now starts without a Gemini key and has a local smoke test for the core fallback path.

## License

MIT
