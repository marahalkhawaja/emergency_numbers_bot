# Homs Emergency Numbers Bot

The project runs the Telegram bot and a read-only JSON REST API together.

## Run

Install the dependencies and set `BOT_TOKEN` in the environment or `.env` file:

```powershell
pip install -r requirements.txt
$env:BOT_TOKEN = "your-telegram-bot-token"
python main.py
```

The API listens on `0.0.0.0:5000` by default. Configure the bind address and
port with `API_HOST` and `API_PORT`:

```powershell
$env:API_HOST = "127.0.0.1"
$env:API_PORT = "8000"
python main.py
```

## Endpoints

- `GET /health` — API health status.
- `GET /services` — all emergency services as a JSON array.
- `GET /services/<service_id>` — one service by its ID; returns `404` for an
  unknown ID.

Each service includes its ID, name, phone number, official source, and message.
For example:

```powershell
curl.exe http://localhost:5000/services
curl.exe http://localhost:5000/services/ambulance
```
