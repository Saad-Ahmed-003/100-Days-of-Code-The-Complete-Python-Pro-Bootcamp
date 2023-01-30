import smtplib
import datetime as dt
import random
import pandas

num = 0
num_1 = 0

data = pandas.read_csv("birthdays.csv")

days = data.day.to_list()
months = data.month.to_list()
years = data.year.to_list()
Emails = data.email.to_list()
names = data.name.to_list()

dict_1 = data.to_dict()
print(dict_1)
for i in dict_1:
    for x in dict_1[i]:
        print(num_1)
    if num > 5:
        num_1 = 0
    elif num < 4:
        num_1 = 1
    num += 1





