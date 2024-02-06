from tkinter import *
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

def runCode():
    code = text.get('1.0',END)
    executedCode = exec(code)

window = Tk()
window.geometry('1400x800')

text = Text(width=170,font=("Terminal",15))
text.pack(side=TOP)

menuBar = Menu(window)
runBar = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='run',menu=runBar)
runBar.add_command(label='run',command=runCode)
window.config(menu=menuBar)
window.mainloop()