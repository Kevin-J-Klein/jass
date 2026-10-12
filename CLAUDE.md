# CLAUDE.md

Anweisungen für Claude Code in diesem Repository. Diese Datei wird nachgeführt,
sobald der Agent etwas wiederholt falsch macht.

## Projekt

Online-Jass (Schieber) für den Browser: 4 Spieler in 2 Teams, online gegeneinander
und gegen Computer-Spieler. Später kommt eine iPhone-App in Swift als weiterer Client dazu.

Das Projekt dient auch als Lernprojekt für Git, CI/CD, Docker und das Arbeiten mit
AI-Agenten. Erkläre darum bei neuen Konzepten kurz, was du machst und warum.

## Architektur

- `backend/app/engine/`: Spiel-Engine als reine Python-Logik, **ohne** Netzwerk-,
  Datenbank- oder Framework-Code. Regeln, gültige Züge, Stiche, Punkte.
- `backend/app/bots/`: Computer-Spieler. Sie nutzen nur die öffentliche API der Engine.
- `backend/app/main.py`: FastAPI-App mit HTTP-Endpunkten und WebSockets.
- `frontend/`: React mit TypeScript und Vite (ab Phase 4, existiert noch nicht).
- `protocol/`: JSON Schema für alle WebSocket-Nachrichten (ab Phase 5).

### Grundsätze

- **Der Server entscheidet.** Der Server hält den ganzen Spielzustand und prüft jeden
  Zug. Ein Client bekommt nur seine eigenen Karten und sendet nur Spielzüge.
- **Die Regeln stehen in `RULES.md`.** Bei Widersprüchen zu deinem eigenen Wissen über
  Jass gilt immer `RULES.md`. Ist eine Regel dort unklar oder fehlt sie: fragen, nicht raten.
- **Einstellungen pro Spielraum:** Kartenbild (deutsch/französisch), Trumpf-Faktoren
  an/aus, Zielpunktzahl. Standard: ohne Faktoren, 1000 Punkte.
- **Protokoll versioniert:** Jede Nachricht hat ein Feld `type` und das Protokoll eine
  Versionsnummer. Keine inkompatiblen Änderungen ohne neue Version.

## Befehle

Alle Befehle aus dem Ordner `backend/`:

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt   # Abhängigkeiten installieren
ruff check .                          # Linting
ruff format --check .                 # Formatierung prüfen
pytest                                # Tests
uvicorn app.main:app --reload         # Server lokal starten (http://localhost:8000)
```

Mit Docker, aus dem Hauptordner:

```bash
docker compose up --build
```

## Arbeitsweise

- Arbeite nie direkt auf `main`. Pro Aufgabe ein Branch, z.B. `feature/stichauswertung`
  oder `fix/punkte-letzter-stich`.
- Mach zuerst einen kurzen Plan und warte auf Freigabe, bevor du grössere Änderungen machst.
- Für Spielregeln: **zuerst Tests** mit konkreten Spielsituationen, dann die Umsetzung.
- Kleine, fokussierte Commits. Commit-Nachrichten im Format
  [Conventional Commits](https://www.conventionalcommits.org/), z.B.
  `feat(engine): stichauswertung für obenabe`.
- Vor jedem Commit müssen `ruff check`, `ruff format --check` und `pytest` grün sein.
- Keine neuen Abhängigkeiten ohne Rückfrage.
- Nie Secrets, Passwörter oder `.env`-Dateien committen.

## Code-Stil

- Python 3.12, Type Hints überall, Datenklassen oder Enums statt loser Dicts und Strings.
- Code, Bezeichner und Kommentare auf Englisch. Jass-Begriffe dürfen Schweizerdeutsch
  bleiben, wenn es keine gute Übersetzung gibt (z.B. `obenabe`, `undenufe`, `stoeck`, `weis`).
- Testnamen beschreiben die Situation, z.B.
  `test_under_is_highest_trump_card`.
