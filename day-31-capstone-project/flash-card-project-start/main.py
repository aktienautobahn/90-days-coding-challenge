
# ---------------------------- IMPORT PACKAGES ----------------------------- #
from tkinter import *
from tkinter import messagebox
import pandas as pd
from random import choice
# ---------------------------- SET FILE PATHS --------------------------- # 
import os
here = os.path.dirname(os.path.abspath(__file__))
print(here)
card_back = os.path.join(here, 'images/card_back.png')
card_front = os.path.join(here, 'images/card_front.png')
right = os.path.join(here, 'images/right.png')
wrong = os.path.join(here, 'images/wrong.png')
data = os.path.join(here, 'data/french_words.csv')
words_to_learn = os.path.join(here, 'data/words_to_learn.csv')
# ---------------------------- CONSTANTS ------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"
CARD_BACKGROUND_COLOR = "#92c1af"
FONT_NAME = "Ariel"
DELAY = 3000

# ----------------------------  LOAD WORDS ----------------------------- #

def load_words():

    try:
        try:
            words_df = pd.read_csv(words_to_learn)
            words = words_df.to_dict(orient="records")
            if len(words) == 0:
                words_df = pd.read_csv(data)
                words = words_df.to_dict(orient="records") 
                
        except:
            words_df = pd.read_csv(data)
            words = words_df.to_dict(orient="records")
            
    except FileNotFoundError:
        messagebox.showerror(title="No words files found", message="Words files are not found")

    else:
        return words

# ---------------------------- RIGHT BUTTON CLICKED ----------------------------- #
def right_button_clicked():
    #delete word from the list words
    try:
        words.remove(picked_word)
        print(f"{picked_word} is removed")
    except ValueError:
        pass
    finally:
        word_picker()

# ---------------------------- WRONG BUTTON CLICKED ----------------------------- #

def wrong_button_clicked():
    #save word into a list_to_remember
    global list_to_remember
    list_to_remember.append(picked_word)
    list_to_remember_df = pd.DataFrame.from_dict(list_to_remember)

    try:
        save_df = pd.read_csv(words_to_learn)
        save_df = save_df.append(list_to_remember_df, ignore_index=True)
        save_df.drop_duplicates(keep=False,inplace=True)
        pass
    except:
        save_df = list_to_remember_df
    
    finally:

        save_df.to_csv(words_to_learn, index=False)
        word_picker()


# ---------------------------- RANDOM WORD PICKER ----------------------------- #
def word_picker():
    global picked_word
    
    try:
        picked_word = choice(words)

    except IndexError:
    
        picked_word = words[0]

    finally:
        canvas.itemconfigure(canvas_image, image=card_front_img)
        language.config(text=[key for key in picked_word.keys()][0], bg="white")
        front_word.config(text=[value for value in picked_word.values()][0], bg="white")
        timer_object = window.after(DELAY, card_flipper)
        #messagebox.showinfo(title="No words", message="There are not word to choice from")

# ---------------------------- FLIP CARS MECHANISM ----------------------------- #
def card_flipper():
    canvas.itemconfigure(canvas_image, image=card_back_img)
    language.config(text=[key for key in picked_word.keys()][1], bg=CARD_BACKGROUND_COLOR)
    front_word.config(text=[value for value in picked_word.values()][1], bg=CARD_BACKGROUND_COLOR)    

# ---------------------------- LIST-TO-LEARN-CREATOR ----------------------------- #
def to_lern():
    pass

# ---------------------------- GLOBAL VARIABELS ----------------------------- #
picked_word = {}
list_to_remember = []
words = load_words()

# ---------------------------- GUI BUILDER ----------------------------- #



window = Tk()
window.title("Flash Cards")
window.config(padx=40, pady=50, bg=BACKGROUND_COLOR)


#card back image
canvas = Canvas(width=800, height=528, bg=BACKGROUND_COLOR, highlightthickness=0)

#load images
card_back_img = PhotoImage(file=card_back)
card_front_img = PhotoImage(file=card_front)
right_img = PhotoImage(file=right)
wrong_img = PhotoImage(file=wrong)

canvas_image = canvas.create_image(400, 264, image=card_front_img)
#timer_text = canvas.create_text(400, 264, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


#word labels
language = Label(text="Press right button to start", bg="white", font=(FONT_NAME, 40, "italic"), highlightthickness=0)
language.place(anchor="center", x=400, y=150)

front_word = Label(text="",  bg="white", font=(FONT_NAME, 60, "bold"), highlightthickness=0)
front_word.place(anchor="center", x=400, y=263)


#buttons
right_button = Button(image=right_img, highlightbackground=BACKGROUND_COLOR, highlightthickness=0, command=right_button_clicked)
right_button.grid(column=1,row=1)

wrong_button = Button(image=wrong_img, highlightbackground=BACKGROUND_COLOR, highlightthickness=0, command=wrong_button_clicked)
wrong_button.grid(column=0,row=1)

window.mainloop()


