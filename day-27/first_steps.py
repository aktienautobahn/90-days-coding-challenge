from tkinter import Tk, Label, Button, Entry

window = Tk()
window.minsize(width=500, height=300)

my_label = Label(text="I am a label", font=("Arial",24,"bold"))
my_label.pack()


#my_label['text'] = "My new text"


#button function
def button_click():
    my_label.config(text = input.get())

#Input field

input = Entry(width=10)
input.pack()

#Button

button = Button(text='Click me',command=button_click)
button.pack()









window.mainloop()