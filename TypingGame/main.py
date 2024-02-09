import time
import random
from tkinter import *
from tkinter import ttk
from sampleSentences import sentences
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

BG_COLOR = "#34245e"
BG_COLOR_2 = "#655199"
FG_COLOR = "white"
COUNTDOWN_START = 4

count = COUNTDOWN_START
sampleSentences = sentences()
startTime = 0
currentSentence = ""

def calculate_accuracy(user_input, sentence):
    user_words = user_input.strip().split()
    sentence_words = sentence.strip().split()
    correct_words = [uw == sw for uw, sw in zip(user_words, sentence_words)]
    accuracy = (sum(correct_words)) / len(sentence_words)
    return round(accuracy * 100), len(sentence_words)

def submit():
    global startTime, currentSentence
    userInput = userEntry.get(1.0, END)
    accuracy, sentence_length = calculate_accuracy(userInput, currentSentence)
    typingTime = round(time.time() - (startTime+1), 2)
    wpm = round((sentence_length / typingTime) * 60)
    timeWpm.config(text=f"Time: {typingTime} seconds\nAccuracy: {accuracy}%\nWPM: {wpm}")

def start(event):
    global startTime, count
    window.unbind("<space>")
    count -= 1
    if count > 0:
        practiceSentence.config(text=f"{count}")
        window.after(1000, start,event)
    else:
        global currentSentence
        currentSentence = random.choice(sampleSentences)
        practiceSentence.config(text=currentSentence)
        userEntry.config(state="normal")
        startTime = time.time()

def newSentence():
    global startTime
    global currentSentence
    currentSentence = random.choice(sampleSentences)
    practiceSentence.config(text=currentSentence)
    userEntry.config(state="normal")
    timeWpm.config(text="")
    userEntry.delete(1.0,END)
    startTime = time.time()

window = Tk()
window.geometry("900x400")
window.title('Typing Test')
window.resizable(False, False)
window.bind("<space>", start)
window.config(bg=BG_COLOR)

menubar = Menu(window)
window.config(menu=menubar)
colorMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Color Changer", menu=colorMenu)
colorMenu.add_command(label="apple")

practiceSentence = Message(
    font=('Consolas', 15),
    width=700,
    bg=BG_COLOR,
    fg=FG_COLOR,
    text="Welcome to this typing test! Press spacebar to get started and the enter key when you are finished with the sentence"
)
practiceSentence.grid(row=0, column=0)

userEntry = Text(
    font=('Consolas', 15),
    width=50,
    height=3,
    state="disabled",
    bg=BG_COLOR_2,
    fg=FG_COLOR,
    wrap="word"
)
userEntry.grid(row=1, column=0)

timeWpm = Message(font=('Consolas', 15), width=700, bg=BG_COLOR, fg=FG_COLOR)
timeWpm.grid(row=3, column=0)

submitBtn = Button(text="Submit", command=submit, font=('Consolas', 15))
submitBtn.grid(row=2, column=0)

newSentenceBtn = Button(text="New Sentence", command=newSentence, font=('Consolas', 15))
newSentenceBtn.grid(row=1, column=1)

window.mainloop()
