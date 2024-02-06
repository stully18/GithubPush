from api_request import ai
from tkinter import *
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

def api_answer():
    entry = entry_prompt.get("1.0", "end-1c")  # Modified to get the text from the Text widget
    ai_response = ai(entry)
    label_msg.config(text=ai_response)
    window.update()

window = Tk()

window.title('Chat GPT Bot')
window.resizable(False,False)
window.config(bg='#0f6b3d')
label_prompt = Label(text='Prompt:', font=("Courier New",15,'bold'),bg='#0f6b3d',fg="#c2ffe1")
label_prompt.grid(row=0,column=0)
label_msg = Message(text='', font=("Courier New",15),bg='#0f6b3d',fg="#c2ffe1")
label_msg.grid(row=2,column=0,columnspan=2)
entry_prompt = Text(font=("Courier New",15),width=35, height=5,bg="#d4ffe9")
entry_prompt.grid(row=0,column=1)
submit_btn = Button(text='submit', font=("Courier New",15,'bold'),command=api_answer,
                    bg="#0f6b3d",activebackground='#149153',fg="#c2ffe1")
submit_btn.grid(row=1,column=1,columnspan=2)
window.mainloop()
