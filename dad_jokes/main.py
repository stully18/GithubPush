from tkinter import *
from api import *

def change_joke():
    new_joke = get_joke()
    label.config(text=new_joke)

window = Tk()
window.geometry('800x600')
window.title('Dad Jokes')
window.resizable(width=False,height=False)
label = Label(window, text='click below for a joke', font=('ComicSans', 30),
              height=10, wraplength=750)
label.pack(side=TOP)
button = Button(window, text='get joke', font=('ComicSans', 30),
                command=change_joke, bg='#253357',fg='white',
                activebackground='#253357',activeforeground='white',cursor='hand2')
window.config(bg='#6d86c7')
label.config(bg='#6d86c7', fg='white')
button.pack()
window.mainloop()
