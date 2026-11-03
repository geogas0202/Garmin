"""Laedt die Garmin-Zugangsdaten aus .env oder aus den Umgebungsvariablen."""

import os
from pathlib import Path

ENV_FILE = Path(__file__).parent / ".env"


def load_env(path: Path = ENV_FILE) -> None:
    """Liest KEY=WERT-Zeilen aus .env in die Umgebungsvariablen."""
    if not path.exists():
        # Keine .env: Werte kommen direkt aus den Umgebungsvariablen
        # (z.B. aus den Einstellungen der Claude-Code-Umgebung).
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def get(name: str) -> str:
    """Gibt einen Wert zurueck oder meldet, dass er fehlt."""
    value = os.environ.get(name, "")
    if not value:
        raise KeyError(f"{name} ist weder in .env noch als Umgebungsvariable gesetzt.")
    return value


load_env()

if __name__ == "__main__":
    for key in ("GARMIN_EMAIL", "GARMIN_API_KEY", "GARMIN_CONSUMER_KEY"):
        print(f"{key}: {'gesetzt' if os.environ.get(key) else 'leer'}")
