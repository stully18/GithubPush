import random
from tkinter import *
from PIL import Image, ImageTk
import os
from jpeg_png import file_paths

file_paths = file_paths()

def generate_image():
    num = random.randint(0, len(file_paths) - 1)
    img = Image.open(file_paths[num])
    width, height = img.size
    window.geometry(f'{width}x{height+100}')

    real_image = ImageTk.PhotoImage(img)
    label.config(image=real_image)
    label.image = real_image

window = Tk()
window.geometry('500x400')
window.title('Meme Generator')
window.config(bg='#ecc7ff')
label = Label( bg='#ecc7ff')
button = Button(text='Generate Image', font=('Arial', 20), command=generate_image, bg='#d98fff', activebackground='#dd9cff')
label.pack()
button.pack()

window.mainloop()
