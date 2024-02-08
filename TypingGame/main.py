import time
from tkinter import *
from tkinter import ttk
import random
from sampleSentences import sentences
from ctypes import windll

global count
global currentSentence

windll.shcore.SetProcessDpiAwareness(1)
BG = "#34245e"
BG2 = "#655199"
FG = "white"
count = 4
sampleSentences = sentences()
startTime = 0

def submit(event):
    global startTime
    global currentSentence
    userInput = userEntry.get(1.0,END)
    accuracy = calculate_accuracy(userInput, currentSentence)
    typingTime = round(time.time()-startTime,2)
    timeWpm.config(text=f"Your time was {typingTime} seconds and your accuracy was {accuracy}%")
def calculate_accuracy(user_input, sentence):
    user_words = user_input.strip().split()
    sentence_words = sentence.strip().split()
    correct_words = [uw == sw for uw, sw in zip(user_words, sentence_words)]  # Compare each word
    accuracy = sum(correct_words) / len(sentence_words)  # Calculate accuracy
    return accuracy

def start(event):
    global startTime
    global count
    window.unbind("<space>")
    count -= 1
    if count > 0:
        practiceSentence.config(text=f"{count}")
        window.after(1000, start, event)
    else:
        global currentSentence
        currentSentence = random.choice(sampleSentences)
        practiceSentence.config(text=currentSentence)
        userEntry.config(state="normal")
        startTime = time.time()


window = Tk()
window.geometry("720x400")
window.title('Typing Test')

window.resizable(False, False)
window.bind("<Return>", submit)
window.bind("<space>", start)
window.config(bg=BG)
practiceSentence = Message(font=('Consolas', 15), width=700,bg=BG,fg=FG,
                           text="Welcome to this typing test! Press spacebar to get started and the enter key when you are finished with the sentence")
practiceSentence.grid(row=0, column=0)

userEntry = Text(font=('Consolas', 15), width=50, height=3,state="disabled",bg=BG2,fg=FG)
userEntry.grid(row=1, column=0)
timeWpm = Message(font=('Consolas', 15),width=700,bg=BG,fg=FG)
timeWpm.grid(row=2,column=0)

window.mainloop()
