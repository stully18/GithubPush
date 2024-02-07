import time
from tkinter import *
from tkinter import ttk
import random
from sampleSentences import sentences
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

global count
count = 4
sampleSentences = sentences()
startTime = None
def submit(event):
    global startTime
    typingTime = round(time.time()-startTime,2)

    timeWpm.config(text=f"Your time was {typingTime} seconds")
def start(event):
    global startTime

    global count
    window.unbind("<space>")
    count -= 1
    if count > 0:
        practiceSentence.config(text=f"{count}")
        window.after(1000, start, event)
    else:
        practiceSentence.config(text=random.choice(sampleSentences))
        userEntry.config(state="normal")
        startTime = time.time()


window = Tk()
window.geometry("900x400")
window.title('Typing Test')
window.resizable(False, False)
window.bind("<Return>", submit)
window.bind("<space>", start)

practiceSentence = Message(font=('Consolas', 15), width=700, text="Welcome to this typing test! Press spacebar to get started and the enter key when you are finished with the sentence")
practiceSentence.grid(row=0, column=0)

userEntry = Text(font=('Consolas', 15), width=50, height=3,state="disabled")
userEntry.grid(row=1, column=0)

timeWpm = Message(font=('Consolas', 15),width=700)
timeWpm.grid(row=2,column=0)

window.mainloop()
