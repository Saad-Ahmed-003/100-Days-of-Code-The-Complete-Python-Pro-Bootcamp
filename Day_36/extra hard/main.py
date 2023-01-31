import smtplib
import datetime as dt
import random
import pandas

data = pandas.read_csv("birthdays.csv")

my_email = "saadbinsajid03@gmail.com"
My_password = "pmlvgmtjampxfhvj"

dict_1 = data.to_dict()
repeat_range = data.index.stop

now = dt.datetime.now()
date = now.day
month = now.month

num = 0
list_1 = []
list_2 = []
list_3 = [x for x in dict_1]
list_4 = [i for i in range(repeat_range)]
new_dict = {}

PLACEHOLDER = "[NAME]"
letter_file = ["letter_1", "letter_2", "letter_3"]


while repeat_range != num:
    for i in dict_1:
        for x in dict_1[i]:
            if x == num:
                list_1.append(dict_1[i][x])
                if len(list_1) == 5:
                    dict_2 = {k: v for (k, v) in zip(list_3, list_1)}
                    list_1 = []
    new_dict[str(num)] = dict_2
    num += 1


for i in new_dict:
    if month == new_dict[i]['month']:
        if date == new_dict[i]['day']:
            with open(f"letter_templates/{random.choice(letter_file)}.txt") as letter:
                letter_content = letter.read()
                new_letter = letter_content.replace(PLACEHOLDER, new_dict[i]['name'])
                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=My_password)
                    connection.sendmail(from_addr=my_email,
                                        to_addrs=new_dict[i]['email'],
                                        msg=f"Subject:Happy BIRTHDAY!\n\n"
                                            f"{new_letter}")
