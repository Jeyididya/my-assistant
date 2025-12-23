# my-assistant

A lightweight Telegram userbot that replies to incoming private chats using the Gemini API.

This project is intended as a introduction to how to setup userbots in telegram.


## Quickstart

1. Clone this repository and open it locally.
2. Create a Python virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Set the required environment variables. You can use a `.env` or your system environment. Required variables:

- `API_ID` — your Telegram API ID (from my.telegram.org)
- `API_HASH` — your Telegram API hash
- `GEMINI_API_KEY` — your Gemini / Google generative API 
key

4. Run the bot:

```bash
python main.py
```

The script will start the userbot, fetch recent messages within the configured reply window, and send replies where appropriate.

## Configuration

- `NOT_TO_MESSAGE` (in `main.py`)  list of chat IDs to skip (e.g., Telegram system bots like 777000).
- `PROMPT` (in `gemini_reply.py`) 


## Safety & notes

- The bot stores a Telethon session file (`userbot_session.session`) locally. Keep that file safe.



