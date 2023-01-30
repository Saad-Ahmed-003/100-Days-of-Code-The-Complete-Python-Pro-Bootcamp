import smtplib
import datetime as dt
import random

my_Email = "saadbinsajid03@gmail.com"
MY_password = "pmlvgmtjampxfhvj"


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_Email, password=MY_password)
        connection.sendmail(from_addr=my_Email,
                            to_addrs=my_Email,
                            msg=f"Subject:Monday Motivation\n\n"
                                f"{quote}")


