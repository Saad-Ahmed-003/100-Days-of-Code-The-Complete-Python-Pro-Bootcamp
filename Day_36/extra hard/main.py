import smtplib
import datetime as dt
import random
import pandas

data = pandas.read_csv("birthdays.csv")

dict_1 = data.to_dict()
repeat_range = data.index.stop

num = 0
list_1 = []
list_2 = []

while repeat_range != num:
    for i in dict_1:
        for x in dict_1[i]:
            if x == num:
                list_1.append(dict_1[i][x])
                if len(list_1) == 5:
                    list_2.append(list_1)
                    list_1 = []
    num += 1

if 22 in data.day:
    print("fuck")



