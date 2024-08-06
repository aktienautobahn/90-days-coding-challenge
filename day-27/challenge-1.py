import tkinter

#Creating a new window and configurations
window = tkinter.Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
label = tkinter.Label(text="This is old text")
label.config(text="This is new text")
label.grid(column=0, row=0)

#Buttons
def action():
    print("Do something")

#calls action() when pressed
button = tkinter.Button(text="Button", command=action)
button.grid(column=1, row=1)


#calls action() when pressed
button = tkinter.Button(text="New button", command=action)
button.grid(column=2, row=0)

#Entries
entry = tkinter.Entry(width=30)
#Add some text to begin with
entry.insert(tkinter.END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.grid(column=5, row=5)


window.mainloop()