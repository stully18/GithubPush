import time
import random
from tkinter import *
from customtkinter import *
from sampleSentences import sentences
from ctypes import windll
from PIL import Image, ImageTk

windll.shcore.SetProcessDpiAwareness(1)

BG_COLOR = "#34245e"
BG_COLOR_2 = "#655199"
FG_COLOR = "white"
COUNTDOWN_START = 4

count = COUNTDOWN_START
sampleSentences = sentences()
startTime = 0
currentSentence = ""

png_path = r"C:\Users\jabbe\PycharmProjects\GithubPush\TypingGame\photos\GalaxyBackground.png"

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
    timeWpm.configure(text=f"Time: {typingTime} seconds\nAccuracy: {accuracy}%\nWPM: {wpm}")

def start(event):
    global startTime, count
    window.unbind("<space>")
    count -= 1
    if count > 0:
        practiceSentence.configure(text=f"{count}")
        window.after(1000, start,event)
    else:
        global currentSentence
        currentSentence = random.choice(sampleSentences)
        practiceSentence.configure(text=currentSentence)
        userEntry.configure(state="normal")
        startTime = time.time()

def newSentence():
    global startTime
    global currentSentence
    CurrentSentence = currentSentence
    currentSentence = random.choice(sampleSentences)
    if currentSentence == CurrentSentence:
        currentSentence = random.choice(sampleSentences)
    practiceSentence.configure(text=currentSentence)
    userEntry.configure(state="normal")
    timeWpm.configure(text="")
    userEntry.delete(1.0,END)
    startTime = time.time()

window = CTk()
window.geometry("750x400")
window.title('Typing Test')
window.resizable(False, False)
window.bind("<space>", start)


background_image = Image.open(png_path)
background_image = ImageTk.PhotoImage(background_image)

background_label = Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

menubar = Menu(window)
window.configure(menu=menubar)
colorMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Color Changer", menu=colorMenu)
colorMenu.add_command(label="apple")

practiceSentence = Message(
    font=('Consolas', 15),
    bg=BG_COLOR,
    fg=FG_COLOR,
    width=700,
    text="Welcome to this typing test! Press spacebar to get started and the enter key when you are finished with the sentence"
)
practiceSentence.grid(row=0, column=0)

userEntry = CTkTextbox(master=window,
    font=('Consolas', 20),
    width=500,
    height=100,
    state="disabled",
    fg_color=FG_COLOR,
    text_color="black",
    wrap="word"
)
userEntry.grid(row=1, column=0)

timeWpm = Message(font=('Consolas', 15),
                  width=700,
                  bg=BG_COLOR,  # Set background to match window background
                  fg=FG_COLOR)
timeWpm.grid(row=3, column=0)

submitBtn = CTkButton(master=window,
                      text="Submit",
                      command=submit,
                      font=('Consolas', 18),
                      corner_radius=20,
                      fg_color="#937ccc",
                      hover_color="#c3acfa",
                      border_color=BG_COLOR,  # Set border color to match the background
                      border_width=2,
                      width=150,
                      height=30)
submitBtn.grid(row=2, column=0)

newSentenceBtn = CTkButton(master=window,
                           text="New Sentence",
                           command=newSentence,
                           font=('Consolas', 18),
                           corner_radius=20,
                           fg_color="#937ccc",
                           hover_color="#c3acfa",
                           border_color=BG_COLOR,
                           border_width=2,
                           width=150,
                           height=30)
newSentenceBtn.grid(row=1, column=1)

window.mainloop()
