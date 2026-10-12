"""Entry point of the Jass backend."""

from fastapi import FastAPI

app = FastAPI(title="Jass")


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Hoi! Hier entsteht ein Jass."}


@app.get("/health")
def health() -> dict[str, str]:
    """Used by Docker and the hosting platform to check that the server is alive."""
    return {"status": "ok"}
