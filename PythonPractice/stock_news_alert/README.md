# Stock News Alert Trading Bot
<br>
This is a mini-project built in Python to practice API integration and real-time data fetching.
<br>
## Features:
- Fetches real-time stock price data using Stock API
- Filters out yesterdays's and day before Closing Price of Stocks
- Checks and Compares the difference and if it is beyond certain percent(say 5) 
- Sends an Alets to the User via Email and
- Retrieves top news headlines for the selected company using News API 

## How it Works:
1. You choose a company (e.g., Reliance, Amazon, Apple).
2. The script fetches the latest stock price movement.
3. If there's a significant change, it pulls related news headlines.
4. Sends the alert via email.

## Technologies Used:
- Python
- smtplib for sending emails
- requests module for sending API requests
- dotenv module for loading .env and for secure credential storage
- Two public APIs (Stock & News)
<br>
## Setup Instructions:
- Clone the repo
- Set up your .env file with the required API keys and email credentials
- Run main.py

## Note:
- The company names and their stock/news codes are hardcoded for now for flexibility.
