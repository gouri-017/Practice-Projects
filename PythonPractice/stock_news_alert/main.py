import requests
import smtplib
from dotenv import load_dotenv
import os

# loading env file and data from it like api keys and app passwords for sending mail
load_dotenv()
key1_stock_prices = os.getenv("Stock_api")
key2_news = os.getenv("News_api")

sending_mail = os.getenv("mail1").strip()
receiving_mail = os.getenv("mail2").strip()
new_gmail_pass = os.getenv("new_gmail_pass").strip()

def send_mail():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=sending_mail, password=new_gmail_pass)
        connection.sendmail(from_addr=sending_mail, to_addrs=receiving_mail,
                            msg= f"Subject:BUY OR SELL?! \n\n\n Today's Stock Market News Update for {STOCK_NAME}"
                                 f"\n There Has been {diff_percent}% {up_down} in the Stock prices of"
                                 f" {STOCK_NAME}.\n Here's All You need to Know :\n\n {articles}\n Make Your Choice "
                                 f"Today To BUY or SELL. ")



# For now hardcoding the stock values for the program to work
STOCK_NAME = "RELIANCE.BSE" #AMZN for amazon
COMPANY_NAME = 'RELI'  #AMZN

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://api.marketaux.com/v1/news/all"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": key1_stock_prices,
}
news_params ={
    "symbols":COMPANY_NAME,
    'filter_entities':'true',
    "language":'en',
    "api_token": key2_news,
}

articles={}

def fetch_articles():
    """Fetches Latest News Articles for the Stock Company whose price we are comparing. """
    value_e = 0
    for i in range(3):
        news_dictionary = news_data.get('data')[i]
        for (key, value) in news_dictionary.items():
            if key == 'title':
                title_key = value
                articles[title_key] = value_e
            elif key == "url":
                value_e = value
                articles[title_key] = value_e

# Sending Requests for getting the desired company;s Stock prices
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
previous_day_data = data_list[1]
previous_day_closing_price = previous_day_data["4. close"]

# Finding the difference between Yesterday's and Day before's closing price for the Market

difference = float(yesterday_closing_price) - float(previous_day_closing_price)
# print(difference)

if difference < 0:
    up_down = "fall"
else:
    up_down = "rise"
# Finding the Difference percent To Check if there is a Huge Fall or Rise in price
diff_percent = round((difference / float(yesterday_closing_price)) * 100)
diff_percent = abs(diff_percent)
# print(diff_percent)

# if the difference Percent is Huge Getting Some Latest News Articles for that Company and
# Sending mail to  User to Alert Him of the Change

# can change the percent for when to send the message to however we want
if diff_percent >= 1:
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_data = news_response.json()
    fetch_articles()
    print(articles)
    send_mail()

# print(diff_percent)
#
# print(up_down)
# print(yesterday_closing_price)
# print(previous_day_closing_price)

#
