import smtplib
import datetime as dt
import random
import pandas

data = pandas.read_csv("birthdays.csv")

dict_1 = data.to_dict()



for i in dict_1:
    for x in dict_1[i]:
        print(x)
        if




