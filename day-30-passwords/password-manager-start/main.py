from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import os
import json


# ---------------------------- SET FILE PATH --------------------------- # 
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'logo.png')
pass_log = os.path.join(here, "passwords.json")


# ---------------------------- PASSWORD SEARCHER -------------------------------- #

def pass_searcher():
    website = website_entry.get() 
    try:
        with open(pass_log, mode="r") as file:
            data = json.load(file)

        if website in data:

            for ws in data:
                if ws == website:
                    username_entry.delete(0, END) 
                    username_entry.insert(0, data[ws]["username"])
                    password_entry.delete(0, END) 
                    password_entry.insert(0, data[ws]["password"])
        else:
            messagebox.showwarning(title="Oops", message="No entries found")          
    except FileNotFoundError:
        messagebox.showwarning(title="Oops", message="Passwords' log file was not found.")

                   
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def pass_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 
                'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
                'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters= randint(8, 10)
    nr_symbols = randint(2, 4) 
    nr_numbers = randint(2, 4) 

    password = []
    [password.append(choice(letters)) for _ in range(0, nr_letters)]
    [password.append(choice(symbols)) for _ in range(0, nr_symbols)]
    [password.append(choice(numbers)) for _ in range(0, nr_numbers)]

    shuffle(password)
    password_r = ''.join(password)
    password_entry.delete(0, END) 
    password_entry.insert(0, string=password_r)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {

        website: {
            "username": username,
            "password": password
        }
    }

    if website == "" or username == "" or password == "":
        messagebox.showwarning(title="Oops", message="Please complete the text fields before saving")
    else:
        is_okay = messagebox.askokcancel(title=website, message=f"These are details entered: \n\n"
                                                    f"Website: {website}\nUsername: {username}"
                                                    f"\nPassword: {password}\n\nIs it okay to save?")
        if is_okay:
            try:
                with open(pass_log, mode="r") as file:
                    try:
                        data = json.load(file)
                    except:
                        data = {}
            except:
                data = {}
            finally:
                data.update(new_data)    
                with open(pass_log, mode="w") as file:
                    json.dump(data, file, indent=4)

                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
#main window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=50, bg="white")

#MyPass image
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file=filename)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text="Website:",bg="white", font=("Arial",12,"bold"))
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:",bg="white", font=("Arial",12,"bold"))
username_label.grid(column=0, row=2)

password_label = Label(text="Password:",bg="white", font=("Arial",12,"bold"))
password_label.grid(column=0, row=3)

#Text boxes
website_entry = Entry(width=20, highlightthickness=0)
website_entry.grid(column=1, row=1)

username_entry = Entry(width=37, highlightthickness=0)
username_entry.insert(0, string="emilautobahn@gmail.com")
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=20, highlightthickness=0)
password_entry.grid(column=1, row=3)

#Buttons
search_button = Button(text="Search Password", highlightbackground="white", bg="white", 
                            highlightthickness=0, command=pass_searcher)
search_button.grid(column=2, row=1)
gen_pass_button = Button(text="Generate Password", highlightbackground="white", bg="white", 
                            highlightthickness=0, command=pass_gen)
gen_pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, highlightbackground="white", bg="white", 
                    highlightthickness=0, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

#main loop
window.mainloop()