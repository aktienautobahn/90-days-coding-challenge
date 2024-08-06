from ctypes import alignment
import tkinter

#Creating a new window and configurations
window = tkinter.Tk()
window.title("Mile to Km Converter")
#window.minsize(width=100, height=150)

#Labels
label_1 = tkinter.Label(text="is equal to")
label_1.grid(column=0, row=3)

label_2 = tkinter.Label(text="miles")
label_2.grid(column=2, row=2)

label_3 = tkinter.Label(text="km")
label_3.grid(column=2, row=3)


#Buttons
def converter():
    #Gets text in entry
    input = text_field_miles.get()
    result = round(float(input)*1.609 , 2)
    label_km.config(text = result)



#Entries
#input label
text_field_miles = tkinter.Entry(width=10)
#Add some text to begin with
text_field_miles.insert(tkinter.END, string="0")

text_field_miles.grid(column=1, row=2)

#output label
label_km = tkinter.Label(text="0")
label_km.grid(column=1, row=3)

#calls action() when pressed
button = tkinter.Button(text="Calculate", command=converter)
button.grid(column=1, row=4)


window.mainloop()