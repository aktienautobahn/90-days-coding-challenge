from tkinter import *
from turtle import back
import requests
import os

here = os.path.dirname(os.path.abspath(__file__))
backgound_file = os.path.join(here, 'background.png')
kanye_file = os.path.join(here, 'kanye.png')

def get_quote():
    quote_get = requests.get(url="https://api.kanye.rest/")
    quote_dict = quote_get.json()
    quote = quote_dict.get('quote')
    canvas.itemconfig(quote_text, text=quote)



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=backgound_file)
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=kanye_file)
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()