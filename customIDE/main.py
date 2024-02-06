from tkinter import *
from ctypes import windll
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
import os
windll.shcore.SetProcessDpiAwareness(1)

def runCode():
    code = text.get('1.0',END)
    executedCode = exec(code)

window = Tk()
window.geometry('1500x810')
window.config(bg='#5c5c5c')

open_img = PhotoImage(file="C:\PythonImages\IDE\open.png")
save_img = PhotoImage(file="C:\PythonImages\IDE\save.png")
run_img = PhotoImage(file="C:\PythonImages\IDE\\run.png")
text = Text(font=("Consolas",25),width=60,height=21,bg="#3d3d3d",fg="#dbdbdb",borderwidth=0)
text.grid(row=0,column=1,columnspan=2,rowspan=3)
open_btn = Button(image=open_img,bg='#5c5c5c',relief="flat",activebackground='#5c5c5c')
open_btn.grid(row=0,column=0)
save_btn = Button(image=save_img,bg='#5c5c5c',relief="flat",activebackground='#5c5c5c')
save_btn.grid(row=1,column=0)
run_btn = Button(image=run_img,bg='#5c5c5c',relief="flat",activebackground='#5c5c5c')
run_btn.grid(row=2,column=0)
output_code = Message(text='hi ehe hjd hjhfjdhf ojowe rj5534 oj o j',width=300,font=("Consolas",20,'bold'),fg='#14c900',bg='#5c5c5c')
output_code.grid(column=3,row=0)

window.mainloop()