from tkinter import *
import tkinter.ttk as ttk
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

window = Tk()

# Use raw string literals or escape backslashes to avoid SyntaxWarning
theme_file_path = r"\ttkThemes\azure.tcl"

# Load the custom theme file
try:
    window.tk.call("source", theme_file_path)
except TclError as e:
    print(f"Error loading theme file: {e}")

window.tk.call("set_theme", "dark")
style = ttk.Style()
style.theme_use('clam')

window.geometry("800x300")
label = Label(text='Enter URL to scrape:')
web_url = Entry()
searchBtn = Button(text='Scrape')
searchBtn.grid(row=1, column=0, columnspan=2)
label.grid(row=0, column=0)
web_url.grid(row=0, column=1)

window.mainloop()
