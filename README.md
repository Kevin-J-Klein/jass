# Jass

Ein Schieber-Jass für den Browser: online gegen Freunde oder gegen Computer-Spieler.

Lernprojekt für Git, CI/CD, Docker und das Arbeiten mit AI-Agenten (Claude Code).

## Status

Phase 1: Fundament. Ein Hello-World-Backend läuft im Docker-Container, die CI prüft
jeden Pull Request.

## Lokal starten

Ohne Docker:

```bash
cd backend
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

Mit Docker:

```bash
docker compose up --build
```

Danach läuft das Backend auf <http://localhost:8000>. Ob es lebt, zeigt
<http://localhost:8000/health>.

## Tests

```bash
cd backend
ruff check .
ruff format --check .
pytest
```

## Projektstruktur

```
.
├── .github/workflows/ci.yml   CI-Pipeline (GitHub Actions)
├── backend/
│   ├── app/main.py            FastAPI-App
│   ├── tests/                 Tests (pytest)
│   ├── Dockerfile
│   ├── requirements.txt       Abhängigkeiten für den Betrieb
│   └── requirements-dev.txt   zusätzlich für Entwicklung und Tests
├── docker-compose.yml         alles lokal starten
├── CLAUDE.md                  Anweisungen für Claude Code
└── RULES.md                   verbindliche Jass-Regeln
```
