import time
import random
from tkinter import *

import customtkinter
from customtkinter import *
from sampleSentences import sentences
from ctypes import windll
from PIL import Image, ImageTk

windll.shcore.SetProcessDpiAwareness(1)

BG_COLOR = "#34245e"
BG_COLOR_2 = "#655199"
FG_COLOR = "white"
COUNTDOWN_START = 4
global wpm_list
wpm_list = []
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
    global startTime, currentSentence, wpm_list
    userInput = userEntry.get(1.0, END)
    accuracy, sentence_length = calculate_accuracy(userInput, currentSentence)
    typingTime = round(time.time() - (startTime+1), 2)
    wpm = round((sentence_length / typingTime) * 60)
    wpm_list.append(wpm)
    averageWpm = int(sum(wpm_list)/len(wpm_list))
    timeWpm.configure(text=f"Time: {typingTime} seconds\nAccuracy: {accuracy}%\nWPM: {wpm}")
    averageWpmLbl.configure(text=f'average wpm: {averageWpm}')

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

window = customtkinter.CTk()
window.geometry("750x400")
window.title('Typing Test')
window.resizable(False, False)
window.bind("<space>", start)




background_image = customtkinter.CTkImage(light_image=Image.open(png_path),
                                          dark_image=Image.open(png_path),
                                          size=(750,400))
img = Image.open(png_path)
uppercroppedPng = img.crop((0,100,250,300))
lowercroppedPng = img.crop((0,300,550,500))
upperlabel_image = customtkinter.CTkImage(light_image=uppercroppedPng,
                                  dark_image=uppercroppedPng,
                                          size=(550,100))

lowerlabel_image = customtkinter.CTkImage(light_image=lowercroppedPng,
                                  dark_image=lowercroppedPng,
                                          size=(550,100))
buttonImage = customtkinter.CTkImage(light_image=lowercroppedPng,
                                     dark_image=lowercroppedPng,
                                     size=(150,30))

background_label = CTkLabel(master=window, image=background_image,text="")
background_label.place(x=0, y=0, relwidth=1, relheight=1)


practiceSentence = CTkLabel(
    master=window,
    font=('Consolas', 20),
    bg_color="transparent",
    text_color="white",
    compound="center",
    image=upperlabel_image,
    fg_color="transparent",
    width=550,
    height=100,
    text="Welcome to this typing test!\nPress spacebar to get started and the enter key\nwhen you are finished with the sentence"
)
practiceSentence.grid(row=0, column=0)

userEntry = CTkTextbox(master=window,
    font=('Consolas', 15),
    width=500,
    height=100,
    state="disabled",
    fg_color=FG_COLOR,
    text_color="black",
    wrap="word"
)
userEntry.grid(row=1, column=0)

averageWpmLbl = CTkLabel(master=window,
                   font=('Consolas', 15),
                   width=100,
                   text_color="white",
                   text="average wpm:",
                   fg_color="#906bff",
                   bg_color="black"
                   )
averageWpmLbl.grid(row=2, column=1)

timeWpm = CTkLabel(master=window,
                   font=('Consolas', 15),
                   width=200,
                   text_color="white",
                   bg_color="transparent",
                   fg_color="transparent",
                   text="",
                   compound="center",
                   image=lowerlabel_image
                   )
timeWpm.grid(row=3, column=0)

submitBtn = CTkButton(master=window,
                      text="Submit",
                      corner_radius=0,
                      command=submit,
                      font=('Consolas', 18),
                      fg_color="#937ccc",
                      hover_color="#c3acfa",
                      border_color="#737373",
                      border_width=3,
                      width=150,
                      height=30)
submitBtn.grid(row=2, column=0,pady=5)

newSentenceBtn = CTkButton(master=window,
                           text="New Sentence",
                           command=newSentence,
                           font=('Consolas', 18),
                           fg_color="#937ccc",
                           corner_radius=0,
                           hover_color="#c3acfa",
                           border_color="#737373",
                           border_width=3,
                           width=150,
                           height=30)
newSentenceBtn.grid(row=1, column=1)

window.mainloop()