# ---------------------------- IMPORT NESSESARY LIBRARIES --------------------------- # 

from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import os
from tkinter.scrolledtext import ScrolledText
import datetime


# ---------------------------- SET FILE PATH --------------------------- # 
here = os.path.dirname(os.path.abspath(__file__))


# ---------------------------- LOGIC ---------------------------- #


class TypingSpeedTest(Tk):
       
    def __init__(self):
        super().__init__()
        self.text = ''
        self.not_started_typing = True
        self.time_counter = 0
        self.sum_elapsed_time = 0
        self.average_key_stroke_time_microseconds = 0
        self.ui_setup()
        
        
    def open_file(self):

        try:
            filename = askopenfilename(initialdir=here, filetypes =[("plain text","*.txt")])
            if filename is not None:
                with open(filename, 'r') as file:
                    self.text = file.readlines()
            
            self.text_processor()
        except FileNotFoundError:
            messagebox.showwarning(title="Oops", message="Please choose text file")
        return


        
    def text_processor(self):
        #TODO process text fluently while typing
        # when the line is equal, add 1 line 
        for line in self.text:
            self.multiline_text.config(state=NORMAL)
            # self.multiline_text.after(DELAY, self.multiline_text.insert(END, line + '\n'))
            self.multiline_text.insert(END, line + '\n')



    
    def cpm_counter(self, *args):
        """
        cpm , or characters per minute ist calculated only while typing. If the user
        doesn't type for a while, which is more than 5x of an average keystoke time, 
        the time counter considers it as a break and doesn't calculate the overtime
        
        """
        
        current_time = datetime.datetime.now()
        
        #first symbol
        if self.not_started_typing:
            self.previous_time = current_time - datetime.timedelta(microseconds=100000)
            self.average_key_stroke_time_microseconds = (current_time - self.previous_time).microseconds / len(self.sv.get())
            self.not_started_typing = False

        typed_time = ( current_time - self.previous_time )
        elapsed_time = int((typed_time.seconds * 1000000) + (typed_time.microseconds))
 
        
        # reset counter in case of break
        if elapsed_time > self.average_key_stroke_time_microseconds*5:
            """
            if the break between typing is more thant 5fold of average key stroke time,
            reset the previous time to the current time minus 100000 microsec
            """
            self.previous_time = current_time - datetime.timedelta(microseconds=100000) 
            typed_time = ( current_time - self.previous_time )
            elapsed_time = int((typed_time.seconds * 1000000) + (typed_time.microseconds))

        self.sum_elapsed_time = self.sum_elapsed_time + elapsed_time

        symbols_min = len(self.sv.get()) / (self.sum_elapsed_time / 60000000)
        # recalculate average key stroke time in microsec
        if len(self.sv.get()) == 0:
            self.average_key_stroke_time_microseconds = self.sum_elapsed_time
        else:
            self.average_key_stroke_time_microseconds = self.sum_elapsed_time / len(self.sv.get())

        self.speed_text.configure(text=round(symbols_min))
        #assign current time as a previous time
        self.previous_time = current_time






         

    
    
    
    def ui_setup(self):

        # ---------------------------- UI SETUP ------------------------------- #
        #main window

        self.title("Typing Speed Test")
        self.config(padx=20, pady=50, bg="grey")
        self.canvas = Canvas(self, width=700, height=500, bg="white", highlightthickness=0)


        # Button
        self.open_btn = Button(text ='Open Text', highlightbackground='grey', command = self.open_file)
        self.open_btn.grid(column=0,row=1)


        # Text area
        self.display_text_label = Label(text="Text:",bg="grey", font=("Arial",16,"normal"))
        self.display_text_label.grid(column=0, row=0, sticky=W)
        
        self.multiline_text = ScrolledText(self, width = 100, height=10, wrap= WORD, background = 'black', font=("Arial",16,"normal"))
        self.multiline_text.grid(column = 1, row = 0, sticky = W)

        # Entry area
        self.sv = StringVar()
        self.sv.trace('w', self.cpm_counter)
        self.input_text = Entry(self, width=100, textvariable=self.sv, validate='key', highlightthickness=0, font=("Arial",16,"normal"))
        self.input_text.insert(0, string='')
        self.input_text.grid(column=1, row=1, columnspan=4 ,sticky=W)
        # Statistics area
        self.stats_label = Label(text="Characters per Minute:",bg="grey", font=("Arial",12,"bold"))
        self.stats_label.grid(column=1, row=2, sticky=E)
        
        self.speed_text = Label(width=20)
        self.speed_text.grid(column=2, row=2, sticky=W)
        



if __name__ == "__main__":
    app = TypingSpeedTest()
    app.mainloop()