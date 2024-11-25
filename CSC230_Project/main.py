import customtkinter
from customtkinter import filedialog
from ctypes import windll
from functions import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

windll.shcore.SetProcessDpiAwareness(1)

window = customtkinter.CTk()
window.geometry('1200x700')
window.title("CSC 230 extra credit")

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=probabilities * 1000, alpha=0.5)  # Adjust scaling factor as needed
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Scatter Plot of X and Y probabilities ')

plt.xticks(np.arange(min(x_values), max(x_values)+1, 0.25))

canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().pack(side=customtkinter.RIGHT, fill=customtkinter.BOTH, expand=1)



fileBtn = customtkinter.CTkButton(window, text="select file", command=selectfile)
label = customtkinter.CTkLabel(window, text="testing ", fg_color="transparent",padx=30, font=(" ",25),justify="left")

def getData():
    resultStr = f"""Marginal Distributions:\n {marginal_x.to_string()}\n {marginal_y.to_string()}\n
E[X]={expectedX}\nE[Y]={expectedY}\nVar(X)={varX}\nVar(Y)={varY}\nCov(X,Y)={cov}\nCorrelation={cor}"""
    label.configure(text=resultStr)
getData()

label.pack(side = customtkinter.LEFT)


window.mainloop()