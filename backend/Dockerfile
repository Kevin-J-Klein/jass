# =============================================================================
# Dockerfile für das Jass-Backend
#
# Ein Dockerfile ist ein Rezept: Jede Zeile ist ein Schritt, und jeder Schritt
# erzeugt eine "Schicht" (Layer) im Image. Docker merkt sich die Schichten und
# baut nur neu, was sich geändert hat. Darum ist die REIHENFOLGE wichtig:
# Was sich selten ändert, kommt nach oben.
#
# Deine Aufgabe: Fülle alle Stellen mit "TODO" aus.
# Testen:  docker build -t jass-backend ./backend
#          docker run -p 8000:8000 jass-backend
#          -> http://localhost:8000/health muss {"status":"ok"} zeigen
# =============================================================================


# --- 1. Basis-Image -----------------------------------------------------------
# Jedes Image baut auf einem anderen auf. Wir wollen Python 3.12 in einer
# schlanken ("slim") Variante, das spart mehrere hundert MB.
# Tipp: Suche auf hub.docker.com nach dem offiziellen "python"-Image und
#       schau dir die Tags an.
FROM TODO


# --- 2. Umgebungsvariablen ----------------------------------------------------
# PYTHONDONTWRITEBYTECODE: keine .pyc-Dateien im Container
# PYTHONUNBUFFERED:        Logs sofort ausgeben statt zu puffern
#                          (sonst siehst du in "docker logs" lange nichts)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1


# --- 3. Arbeitsverzeichnis ----------------------------------------------------
# Alle folgenden Befehle laufen in diesem Ordner im Container.
# Tipp: Ein üblicher Name ist /app
WORKDIR TODO


# --- 4. Abhängigkeiten installieren ------------------------------------------
# Wir kopieren ZUERST nur die requirements.txt und installieren die Pakete.
# Frage an dich: Warum nicht gleich den ganzen Code kopieren?
# (Antwort steht ganz unten in dieser Datei.)
#
# Tipp: COPY <quelle auf deinem Mac> <ziel im Container>
#       Pfade auf deinem Mac sind relativ zum Build-Kontext, hier ./backend
COPY TODO TODO

# --no-cache-dir: pip soll keinen Download-Cache im Image liegen lassen
RUN pip install --no-cache-dir -r requirements.txt


# --- 5. Eigenen Code kopieren -------------------------------------------------
# Jetzt erst den Anwendungscode. Wir brauchen nur den Ordner "app",
# nicht die Tests.
COPY TODO TODO


# --- 6. Nicht als root laufen -------------------------------------------------
# Standardmässig läuft alles im Container als root. Das ist ein Sicherheits-
# risiko: Wer eine Lücke in der App findet, hat sofort alle Rechte.
# Wir legen einen einfachen Benutzer an und wechseln zu ihm.
RUN useradd --create-home appuser
USER appuser


# --- 7. Port dokumentieren ----------------------------------------------------
# EXPOSE öffnet nichts, es dokumentiert nur, auf welchem Port die App horcht.
# Welchen Port nutzt uvicorn bei uns? (siehe CMD unten)
EXPOSE TODO


# --- 8. Startbefehl -----------------------------------------------------------
# Das passiert, wenn der Container startet.
# --host 0.0.0.0 ist wichtig: Mit dem Standard 127.0.0.1 wäre die App nur
# INNERHALB des Containers erreichbar, nicht von deinem Mac aus.
#
# Tipp: Die App heisst "app" und liegt in app/main.py, also "app.main:app"
CMD ["uvicorn", "TODO", "--host", "0.0.0.0", "--port", "8000"]


# =============================================================================
# Antwort zu Schritt 4:
# Docker baut eine Schicht nur neu, wenn sich ihre Eingaben geändert haben.
# Ändert sich nur dein Code, bleibt requirements.txt gleich, und Docker nimmt
# die installierten Pakete aus dem Cache. Der Build dauert dann Sekunden
# statt Minuten. Würdest du alles auf einmal kopieren, würde jede Code-
# Änderung eine komplette Neuinstallation aller Pakete auslösen.
# =============================================================================
