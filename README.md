# Real-Time Sports Analysis and Betting Recommendation Bot

This project is a real-time sports analysis bot that monitors live game data, analyzes key metrics, and sends betting recommendations to a designated Telegram group based on pre-defined strategies. The bot uses web scraping to obtain game statistics, applies specific criteria for betting opportunities, and shares recommendations on Telegram for users to act on promptly.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Configuration](#configuration)
6. [Usage](#usage)
7. [File Structure](#file-structure)
8. [Troubleshooting](#troubleshooting)
9. [Future Enhancements](#future-enhancements)
10. [License](#license)

---

## Project Overview
This bot is designed to help users with live sports betting by:
- Collecting and analyzing real-time game data from an online sports statistics site.
- Applying pre-defined strategies based on game metrics such as shots on goal, corners, and game minutes.
- Sending betting recommendations to a Telegram group when conditions meet the specified criteria.

## Features
- **Live Data Scraping**: Continuously fetches live game data to ensure betting recommendations are based on the latest statistics.
- **Pre-defined Betting Strategy**: Checks game metrics against pre-set conditions, such as the number of shots, corners, and game time, before recommending a bet.
- **Automated Telegram Notifications**: Sends formatted betting recommendations directly to a Telegram channel.
- **Error Handling and Logging**: Logs data retrieval, analysis, and notification events for debugging and record-keeping.

## Requirements
- **Python 3.8+**
- **Selenium**: For web scraping and handling JavaScript-loaded content.
- **BeautifulSoup** and **Requests**: For parsing HTML and handling HTTP requests.
- **Telebot (PyTelegramBotAPI)**: For sending messages to Telegram.
- **ChromeDriver**: For running Selenium with Google Chrome in headless mode.

Install dependencies with:
```bash
pip install -r requirements.txt
```

## Installation
1. **Clone this repository**:
   ```bash
   git clone https://github.com/yourusername/sports-betting-recommendation-bot.git
   cd sports-betting-recommendation-bot
   ```
2. **Set up ChromeDriver**:
   - Download ChromeDriver and place it in your PATH or set its path in `api_handler.py` (update `driver_path`).

3. **Set up the Telegram Bot**:
   - Create a bot in Telegram and get the bot token.
   - Set up a chat group and add your bot to it. Retrieve the chat ID for the group.

## Configuration
1. **Telegram Settings**:
   - In `telegram_bot.py`, replace `token` and `chat_id` with your Telegram bot token and chat group ID.

2. **ChromeDriver Path**:
   - Update `driver_path` in `api_handler.py` to point to your ChromeDriver executable.

3. **Betting Strategy**:
   - Customize the betting strategy in `analisar_jogo` function within `main_script.py`. Modify parameters like `minute`, `shots on goal`, `corners`, and other game metrics to match your betting strategy.

## Usage
1. **Start the Bot**:
   - Run the main script to begin data collection, analysis, and Telegram notifications.
   ```bash
   python main_script.py
   ```

2. **Workflow**:
   - The bot scrapes real-time game data, analyzes each game based on pre-set betting criteria, and sends a Telegram message with betting recommendations when conditions are met.

## File Structure
```
├── main_script.py               # Main bot script for data analysis and Telegram messaging
├── api_handler.py               # Script for handling Selenium-based data scraping
├── telegram_bot.py              # Script for sending Telegram messages
├── requirements.txt             # List of Python dependencies
└── fut_trading_bot.log          # Log file for tracking activity
```

## Troubleshooting
- **Data Retrieval Issues**: Ensure the ChromeDriver version matches your Chrome browser version. Adjust `time.sleep()` intervals if the page fails to load.
- **Telegram Message Errors**: Confirm the bot token and chat ID are correctly configured.
- **Selenium Timeout**: If scraping is slow, increase wait times to ensure pages fully load before attempting to retrieve data.

## Future Enhancements
- **Additional Betting Strategies**: Expand the `analisar_jogo` function to support more complex betting criteria.
- **Improved Error Reporting**: Log more detailed error messages and notifications.
- **UI Dashboard**: Create a web-based dashboard to visualize real-time statistics and betting recommendations.
