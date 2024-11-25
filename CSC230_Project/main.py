import customtkinter
from ctypes import windll


windll.shcore.SetProcessDpiAwareness(1)

window = customtkinter.CTk()
window.geometry('1200x700')



window.mainloop()