import tkinter
from customtkinter import CTk, CTkButton, CTkTextbox, CTkLabel, CTkImage
import customtkinter
import ctypes
from PIL import ImageTk, Image
from api_request import request
ctypes.windll.shcore.SetProcessDpiAwareness(2)
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")
def get_response():
    label.configure(state="normal",font=("Arial-BoldMT", 20))
    prompt = entry.get("0.0", "end")
    response = request(prompt)
    label.delete("0.0", "end")
    label.insert("0.0", response)
    entry.delete("0.0", "end")
    label.configure(state="disabled")

app = customtkinter.CTk()
app.title("Google Gemini")
app.geometry("1000x550")
app.minsize(1000,550)
app.maxsize(1000,550)
pil_image = Image.open(r"AI-image\bgimage.png").resize((1000,550))
ctk_image = CTkImage(pil_image, size=(1000,550))
background_label = CTkLabel(app, image=ctk_image,text="")
background_label.place(relx=0.5, rely=0.5,anchor=tkinter.CENTER)
frame = customtkinter.CTkFrame(master=app,width=800, height=450)
label = customtkinter.CTkTextbox(master=frame, font=("Arial-BoldMT", 50), corner_radius=10, wrap="word", state="normal")
label.insert("0.0", "Ask any Question!")
label.configure(state="disabled")
entry = customtkinter.CTkTextbox(master=frame, font=("Arial-BoldMT", 20), corner_radius=10, wrap="word",width=800)
button = customtkinter.CTkButton(master=frame, text="Generate Response", font=("Arial-BoldMT", 30), border_width=3,
                                 border_color="#01467a", corner_radius=20, height=50, command=get_response)

label.grid(row=0, column=0, sticky="nsew", padx=10, pady=(10))
entry.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
button.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
frame.place(relx=0.5, rely=0.5, anchor = tkinter.CENTER)

app.mainloop()
