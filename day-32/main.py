#Monday Motivation Project
import smtplib
import datetime as dt
import random

import os
here = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(here, 'quotes.txt')

MY_EMAIL = "" # add here your email
MY_PASSWORD = "" # add here your key

now = dt.datetime.now()

weekday = now.weekday()

if weekday == 0:
    with open(file, mode="r") as quotes:
        quote = random.choice(quotes.readlines())
    print(quote)


with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg=f"Subject:Monday Motivation\n\n{quote}"
    )