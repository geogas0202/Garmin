# Garmin

Persoenliches Projekt rund um Garmin-Daten.

## Zugangsdaten einrichten

### Ohne Terminal (Claude Code im Browser/App)

Key als Umgebungsvariable in der Claude-Code-Umgebung hinterlegen:
Umgebungsmenue in der Titelleiste der Sitzung -> **Edit** ->
unter *Network secrets* bzw. *Environment variables* eintragen:

```
GARMIN_API_KEY=dein-key
```

Optional auch `GARMIN_EMAIL`, `GARMIN_PASSWORD`, `GARMIN_CONSUMER_KEY`,
`GARMIN_CONSUMER_SECRET`. Gilt ab der naechsten neuen Sitzung.

### Lokal mit Terminal

```bash
cp .env.example .env
```

Dann in `.env` deinen Garmin-Key (und ggf. Login) eintragen.
`.env` steht in `.gitignore` und wird **nie** ins Repository hochgeladen.

Pruefen, ob alles geladen wird:

```bash
python config.py
```

Im eigenen Code:

```python
import config
key = config.get("GARMIN_API_KEY")
```
