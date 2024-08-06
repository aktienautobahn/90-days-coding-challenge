from tkinter import *
import math

# ---------------------------- SET FILE PATH --------------------------- # 
import os
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'tomato.png')

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
delay = 10
reps = 0
check_mark = ""
timer_object = None
# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer_object)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    global reps
    global check_mark
    reps = 0
    check_mark = "" 
    complete_label.config(text=check_mark)



# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    global check_mark
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        countdown(long_break_sec)
        window.state("normal")
        window.attributes('-topmost', 1)
        window.bell()


    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        countdown(short_break_sec)
        window.state("normal")
        window.attributes('-topmost', 1)
        window.bell()

    else:
        title_label.config(text="Work", fg=GREEN) 
        countdown(work_sec)
        window.attributes('-topmost', 0)
        window.bell()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    global delay
    minutes = math.floor(count/60)
    seconds = count % 60

    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    
    if count > 0:
        global timer_object
        timer_object = window.after(delay, countdown, count-1)
    else:
        start_timer()
        check_mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            check_mark += "🍅"
            complete_label.config(text=check_mark)

# ---------------------------- UI SETUP ------------------------------- #

#main window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#Label
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"), highlightthickness=0)
title_label.grid(column=1, row=0)

#tomato image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=filename)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


#start button
start = Button(text="Start", highlightbackground=YELLOW, command=start_timer, )
start.grid(column=0, row=2)

#reset button
reset = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset.grid(column=2, row=2)


#another Label
complete_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"), highlightthickness=0)
complete_label.grid(column=1, row=3)

window.mainloop()
