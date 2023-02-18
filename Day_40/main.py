import smtplib
import requests
from datetime import date, timedelta


connection = smtplib.SMTP()


STOCK_NAME = "TESLA"
COMPANY_NAME = "ibm"


stock_parameters = {
    "function": "TIME_SERIES_DAIL",
    "symbol": "IBM",
    "apikey": "demo"
}


news_parameters = {
    "q": COMPANY_NAME,
    "searchIn": "title",
    "apiKey": "bacd459297c34e5f8fb3983d47456ac0"
}


today = date.today()
yesterday = date.today() - timedelta(1)
yesterday2_0 = date.today() - timedelta(2)


STOCK_ENDPOINT = \
    "https://www.alphavantage.co/query"
NEWS_ENDPOINT = \
    "https://newsapi.org/v2/everything"


response1 = requests.get(
    url=
    "https://www.alphavantage.co/query"
    "?function=TIME_SERIES_DAILY"
    "&symbol=IBM"
    "&apikey=demo"
)
dict_1 = response1.json()


response2 = requests.get(
    url=NEWS_ENDPOINT,
    params=news_parameters
)
dict_2 = response2.json()


print(dict_1)
print(dict_2)
print(yesterday, yesterday2_0)


closing_stock_price_day1 = \
    dict_1["Time Series (Daily)"][str(yesterday)]["4. close"]
closing_stock_price_day2 = \
    dict_1["Time Series (Daily)"][str(yesterday2_0)]["4. close"]


print(closing_stock_price_day1, closing_stock_price_day2)

dif = float(closing_stock_price_day1) - float(closing_stock_price_day2)

dif = "{:.4f}".format(dif)
print(dif)


percentage =\
        ((
                 float(closing_stock_price_day1) - float(closing_stock_price_day2)
        ) / (
                (float(closing_stock_price_day1) + float(closing_stock_price_day2)
                 ) / 2))*100
final_percentage = None

print(percentage)

if float(dif) < 0.0:
    final_percentage = f"🔻{percentage:.1f}%"
elif float(dif) > 0.0:
    final_percentage = f"🔺{percentage:.1f}%"

print(final_percentage)

if percentage > 5.0:
    for i in range(3):
        print(f'Title: {dict_2["articles"][i]["title"]}')
        print(f'description: {dict_2["articles"][i]["description"]}')

