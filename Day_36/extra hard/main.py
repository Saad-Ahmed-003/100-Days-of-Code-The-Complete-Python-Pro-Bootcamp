import smtplib
import datetime as dt
import random
import pandas

data = pandas.read_csv("birthdays.csv")

days = data.day.to_list()
months = data.month.to_list()
years = data.year.to_list()
Emails = data.email.to_list()
names = data.name.to_list()









