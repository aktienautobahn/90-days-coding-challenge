# ---------------------------- IMPORT NESSESARY LIBRARIES --------------------------- # 
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox
from PIL import Image, ImageFont, ImageDraw, ImageTk
import os


# ---------------------------- SET FILE PATH --------------------------- # 
here = os.path.dirname(os.path.abspath(__file__))


# ---------------------------- LOGIC ---------------------------- #

def resize_image(image):
    #resizing image to the basewidth keeping aspect ratio
    basewidth = 500
    wpercent = (basewidth / float(image.size[0]))
    hsize = int((float(image.size[1]) * float(wpercent)))
    resized_image = image.resize((basewidth, hsize), Image.Resampling.LANCZOS)
    #convert to image object
    return ImageTk.PhotoImage(resized_image)
    

def open_file():
    global image_for_watermark
    global image_widget
    global window

    filename = askopenfilename(initialdir=here, filetypes =[("jpeg","*.jpg"),("png","*.png")])
    if filename is not None:
        image_for_watermark = Image.open(filename)
        opened_img = resize_image(image_for_watermark)
        
        # Create a  Widget to display the text or Image
        image_widget = Label(window)
        image_widget.configure(image=opened_img)
        image_widget.image = opened_img 
        image_widget.grid(column=0, row = 0, columnspan=3)


def save_file():

    try:
        # Choose file name
        img_filename = asksaveasfilename(initialdir=here, filetypes =[("jpeg","*.jpg"),("png","*.png")])

        watermark_image.save(img_filename)
    except NameError:
        messagebox.showwarning(title="Oops", message="Please choose image (name) first")
        return
    except ValueError:
        messagebox.showwarning(title="Oops", message="Unknown file extension")
        return
    
def watermarking():
    global watermark_image
    
    try:
        watermark_image = image_for_watermark.copy()
        draw = ImageDraw.Draw(watermark_image)

        # define watermark size
        if watermark_text_size.get() is not None:
            fontsize = watermark_text_size.get()
        else:
            fontsize = 15
        font = ImageFont.truetype('/Library/Fonts/Arial Unicode.ttf', size=int(fontsize)) # for Mac

        # define watermark position
        if watermark_text_pos.get() is not None:
            watermark_pos = watermark_text_pos.get().split(',')
            watermark_pos_x = int(watermark_pos[0])
            watermark_pos_y = int(watermark_pos[1])
        else:
            watermark_pos_x = 10
            watermark_pos_y = 0
        # add Watermark
        draw.text((watermark_pos_x, watermark_pos_y), watermark_text.get(), (255, 255, 255, 50), font=font)
        # resize image
        watermarked_img = resize_image(watermark_image)
        # update image
        image_widget.configure(image=watermarked_img)
        image_widget.image = watermarked_img
        image_widget.grid(column=0, row=0, columnspan=3)
    except NameError:
        messagebox.showwarning(title="Oops", message="Please open an image first")
        return


# ---------------------------- UI SETUP ------------------------------- #
#main window
window = Tk()
window.title("Watermark Manager")
window.config(padx=20, pady=50, bg="grey")

#MyPass image
canvas = Canvas(window, width=500, height=400, bg="white", highlightthickness=0)


# Buttons
open_btn = Button(text ='Open image', highlightbackground='grey', command = open_file)
open_btn.grid(column=0,row=1)

watermark_btn = Button(text = 'Insert Watermark', highlightbackground='grey', command = watermarking)
watermark_btn.grid(column=2, row=2, sticky=NW)

save_btn = Button(text='Save', highlightbackground='grey', command = save_file)
save_btn.grid(column=2, row=1)

# Text boxes labels
watermark_label = Label(text="Watermark text:",bg="grey", font=("Arial",12,"bold"))
watermark_label.grid(column=0, row=2, sticky=W)

watermark_size = Label(text="Watermark size:",bg="grey", font=("Arial",12,"bold"))
watermark_size.grid(column=0, row=3, sticky=W)

watermark_position = Label(text="Watermark pos. X,Y:",bg="grey", font=("Arial",12,"bold"))
watermark_position.grid(column=0, row=4, sticky=W)

# Text boxes
watermark_text = Entry(width=20, highlightthickness=0)
watermark_text.insert(0, string='Watermark dummy text')
watermark_text.grid(column=1, row=2, sticky=W)

watermark_text_size = Entry(width=5, highlightthickness=0)
watermark_text_size.insert(0, string='15')
watermark_text_size.grid(column=1, row=3, sticky=NW)

watermark_text_pos = Entry(width=10, highlightthickness=0)
watermark_text_pos.insert(0, string='10,0')
watermark_text_pos.grid(column=1, row=4, sticky=W)

#main loop
window.mainloop()