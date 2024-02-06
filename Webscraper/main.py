from tkinter import *
import tkinter.ttk as ttk
from ctypes import windll
from request import scrape_page

def scrape():
    url = web_url.get()
    atrribute = element.get()
    if atrribute == "Paragraphs":
        atrribute = 'p'
    elif atrribute == "Links":
        atrribute = "a"
    scraped_page = scrape_page(url,atrribute)
    results.config(text=scraped_page)


windll.shcore.SetProcessDpiAwareness(1)

window = Tk()
style = ttk.Style()
window.tk.call('source',"azure/azure.tcl")
window.tk.call('set_theme','dark')
window.geometry("800x300")

label = Label(text='Enter URL to scrape:',font=('Lato',15))
web_url = ttk.Entry(font=('Lato',15),width=30)
searchBtn = ttk.Button(text='Scrape',command=scrape)
results = Message(font=('Lato',15),width=700)
element_choices = ["Paragraphs","Links"]
element = ttk.Combobox(font=('Lato',15),values=element_choices)
element.current(0)
elementLbl = Label(text='What element would you like to search for?',font=('Lato',15))
elementLbl.grid(row=1,column=0)
element.grid(row=1,column=1)
results.grid(row=3,column=0,columnspan=2)
searchBtn.grid(row=2, column=0, columnspan=2)
label.grid(row=0, column=0)
web_url.grid(row=0, column=1)

window.mainloop()
