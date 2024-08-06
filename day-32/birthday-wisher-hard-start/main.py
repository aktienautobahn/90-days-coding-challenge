##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# ---------------------------- IMPORT PACKAGES ---------------------------- #
import smtplib
import datetime as dt
import random
import pandas as pd
import os

# ---------------------------- PATHS ---------------------------- #
here = os.path.dirname(os.path.abspath(__file__))
birthday_file = os.path.join(here, 'birthdays.csv')
letter_templates = os.path.join(here, "letter_templates", random.choice(["letter_1.txt", "letter_2.txt", "letter_3.txt"]) )

# ---------------------------- CONSTANTS ----------------------------#
PLACEHOLDER = '[NAME]'
MY_EMAIL = "" # add here your email
MY_PASSWORD = "" # add here your key

# ---------------------------- MAIN CODE BLOCK ----------------------------#
#get today's data
now = dt.datetime.now()
day_today = now.day
month_today = now.month


#read birthday file and create a dictionary out of it
birthday_list = pd.read_csv(birthday_file)
birthday_dict = birthday_list.to_dict(orient="records")
#read template which was choisen randomly
with open(letter_templates) as letter_file:
    letter_contents = letter_file.read()

#get the list of birthdays for today
todays_birthdays = [item for item in birthday_dict if item["month"] == month_today and item["day"] == day_today]

# create letter and send it
for item in todays_birthdays:

    new_letter = letter_contents.replace(PLACEHOLDER, item["name"])
    #send letter
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=item["email"],
            msg=f"Subject:Today is your day! Happy birthday!!!\n\n{new_letter}"
            )