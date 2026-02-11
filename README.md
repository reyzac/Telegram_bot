# Telegram AI Assistant

> **Work in Progress**

A Telegram bot that helps organize tasks sent by the user. When a link is sent (e.g. a TikTok link), the bot automatically detects it and downloads the video.

## Features

- Receive and process messages from Telegram
- Detect TikTok links and automatically download videos
- Track processed messages to avoid duplicate handling

## Setup

1. Clone the repository
2. Create a `.env` file with your Telegram bot token:
   ```
   TG_TOKEN=your_telegram_bot_token
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   python -m playwright install
   ```
4. Run the bot:
   ```bash
   python main.py
   ```
