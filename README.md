# Silver Spot Price Tracker

Tracks daily silver spot price, logs to database, and sends a summary email at 07:00 AM CDT with previous day, week, and month activity.

## Features

- Daily price fetch from Metals-API
- Stores historical prices in SQLite
- Sends daily email report via SMTP (Gmail)
- Reports previous trading day, week, month stats
- Configurable schedule and recipients

## Setup

1. Clone/download the repo
2. Install requirements:  
   `pip install -r requirements.txt`
3. Get [Metals-API key](https://metals-api.com/)
4. Create a `.env` file (see sample above)
5. (For Gmail: enable App Passwords if 2FA enabled)
6. Run:  
   `python app.py`

## Scheduling

- The app uses APScheduler and will run daily at 07:00 CDT.
- Keep it running in a screen/tmux session, or use a process manager.

## Notes

- Free Metals-API keys may have usage limits.
- The database will grow slowly; prune as needed.
