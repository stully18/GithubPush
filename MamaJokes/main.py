import customtkinter
from customtkinter import *
from PIL import Image, ImageTk
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

window = customtkinter.CTk()
window.geometry("700x500")



window.mainloop()