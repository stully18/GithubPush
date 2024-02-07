from tkinter import *
from tkinter import ttk
import time
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)
def doSomething(event):
    practiceSentence.config(text="look retard you know how something works")
window = Tk()
window.geometry("900x400")
window.title('Typing Test')
window.bind("<Return>",doSomething)
practiceSentence = ttk.Label(font=('Consolas',15))
practiceSentence.grid(row=0,column=0)
userEntry = ttk.Entry(font=('Consolas',15),width=50)
userEntry.grid(row=1,column=0)



window.mainloop()