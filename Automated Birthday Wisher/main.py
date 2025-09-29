##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas as pd
import random
import smtplib

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()

birthday_list = pd.read_csv("birthdays.csv")

month = 0
day = 0
name = ""
email = ""
for m in birthday_list['month']:
    if m == today.month:
        month = m
    for d in birthday_list['day']:
        if d == today.day:
            day = d
    if day != 0 and month != 0:
        mask = (birthday_list['month'] == month) & (birthday_list['day'] == day)
        name = birthday_list[mask].name[0]
        email = birthday_list[mask].email[0]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
list = ['letter_1.txt','letter_2.txt','letter_3.txt']

if month != 0 and day != 0:
    letter = random.choice(list)

    with open('letter_templates/'+letter) as file:
        birthday_letter = file.readlines()
        birthday_letter[0] = birthday_letter[0].replace("[NAME]",name)

    print(birthday_letter)
# # 4. Send the letter generated in step 3 to that person's email address.

    my_email = "send-email"
    password = "app-password"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=email,
                            msg="".join(birthday_letter))



