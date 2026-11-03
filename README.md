# Garmin

Persoenliches Projekt rund um Garmin-Daten.

## Zugangsdaten einrichten

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
