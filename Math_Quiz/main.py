from tkinter import *
from number_generator import *
import time
from time import sleep
equation,equation_ans = random_equation()
def check_answer():
    an = entry.get()
    ans = int(an)
    print((equation_ans))
    print((ans))
    if ans == equation_ans:
        label.config(text='correct answer')
        time.sleep(1)
        random_equation()
        label.config(text=equation)
    else:
        label.config(text='wrong answer')
        time.sleep(1)
        random_equation()
        label.config(text=equation)
window = Tk()
label = Label(window, font=('Arial',30), text='test')
label.grid(row=0,column=0)
entry = Entry(window, font=('Arial',30))
entry.grid(row=1,column=0)
button = Button(window, font=('Arial',30), command=check_answer,text='submit')
button.grid(row=2,column=0,columnspan=2)
window.mainloop()