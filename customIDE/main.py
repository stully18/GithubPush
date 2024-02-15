import customtkinter
from customtkinter import *
from PIL import Image, ImageTk
from ctypes import windll
import subprocess

windll.shcore.SetProcessDpiAwareness(1)

def runCode():
    code = text.get('1.0',END)
    try:
        result = subprocess.run(["python", "-c", code], capture_output=True, text=True)
        output = result.stdout
        outputLabel.configure(state='normal')
        outputLabel.delete("1.0", END)
        outputLabel.insert("1.0", output)
        outputLabel.configure(state='disabled')
    except subprocess.CalledProcessError as e:
        outputLabel.configure(state='normal')
        outputLabel.delete("1.0", END)
        outputLabel.insert("1.0", "Error: " + str(e))
        outputLabel.configure(state='disabled')

def openFile():
    filepath = filedialog.askopenfilename()
    file = open(filepath,'r')
    fileText = file.read()
    text.delete("1.0",END)
    text.insert("1.0",fileText)

def saveFile():
    file = filedialog.asksaveasfilename(defaultextension='.py',
                                        filetypes=[
                                            ("Python File", ".py")
                                        ])
    fileText = str(text.get(1.0,END))
    with open(file,'w') as file:
        file.write(fileText)
        file.close()

window = customtkinter.CTk()
window.geometry('1200x700')

open_img = customtkinter.CTkImage(light_image=Image.open("C:\\PythonImages\\IDE\\open.png"),
                                  dark_image=Image.open("C:\\PythonImages\\IDE\\open.png"),
                                  size=(100,100))
save_img = customtkinter.CTkImage(light_image=Image.open("C:\\PythonImages\\IDE\\save.png"),
                                  dark_image=Image.open("C:\\PythonImages\\IDE\\save.png"),
                                  size=(100,100))
run_img = customtkinter.CTkImage(light_image=Image.open("C:\\PythonImages\\IDE\\run.png"),
                                  dark_image=Image.open("C:\\PythonImages\\IDE\\run.png"),
                                  size=(100,100))
text = CTkTextbox(master=window,font=("Consolas",20),width=800,height=600,fg_color="#3d3d3d",text_color="#dbdbdb",wrap="word")
text.grid(row=0,column=1,columnspan=2,rowspan=3)
open_btn = CTkButton(master=window,image=open_img,text='',fg_color='transparent',command=openFile)
open_btn.grid(row=0,column=0)
save_btn = CTkButton(master=window,image=save_img,text='',fg_color='transparent',command=saveFile)
save_btn.grid(row=1,column=0)
run_btn = CTkButton(master=window,image=run_img,text='',fg_color='transparent',command=runCode)
run_btn.grid(row=2,column=0)
outputLabel = CTkTextbox(master=window,font=("Consolas",20),width=200,height=600,state='disabled')
outputLabel.grid(row=0,column=3,rowspan=3)

window.mainloop()