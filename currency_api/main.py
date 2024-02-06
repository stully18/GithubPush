from tkinter import *
from tkinter import ttk
from api import  get_api


euro_rate = get_api()
def display_conversion():
    try:
        USD = int(entry.get())
        Euros = round(euro_rate*USD,2)
        label2.config(text=Euros)
    except ValueError:
        label2.config(text='Please only enter a numbers')


window = Tk()
window.title('Euro Conversion Rate')
window.geometry('500x200')
window.resizable(False,False)
label = Label(text='USD to EUR',font=('Euphemia',20,'bold'),padx=10)
label.grid(row=0,column=0)
entry = Entry(font=('Euphemia',20,))
entry.grid(row=0,column=1)
label2 = Label(font=('Euphemia',20),pady=10)
label2.grid(row=3,column=0,columnspan=2)
button = Button(text='submit',command=display_conversion,font=('Euphemia',15))
button.grid(row=1,column=0,columnspan=2)


window.mainloop()