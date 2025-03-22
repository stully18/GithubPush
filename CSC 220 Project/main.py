import timeit
import customtkinter as tk
import multiprocessing
import psutil
from tkinter import *
from functions import threadedPrime, calculatePrimeNumbers

maxThreads = multiprocessing.cpu_count()

def getValues():
    threads = int(threadEntry.get())
    iterations = int(iterationEntry.get())
    end = int(numberEntry.get())
    return threads, iterations, end

def get_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1, percpu=False)
    cpuUsageLabel.configure(text=f"CPU Usage: {cpu_percent}%")
    app.after(1000, get_cpu_usage) 

def calculate():
    resultLabel.configure(text="Calculating...")
    app.update()
    threads, iterations, end = getValues()
    time_multiThreaded = timeit.timeit(lambda: threadedPrime(end, threads), number=iterations)
    time_singleThread = timeit.timeit(lambda: calculatePrimeNumbers(1, end), number=iterations)
    resultConfig(time_singleThread, time_multiThreaded, iterations)

def resultConfig(singleThreadTime, multiThreadTime, iterations):
    resultLabel.configure(text=f"Single thread: {round(singleThreadTime/iterations, 4)} seconds\nMulti-threaded: {round(multiThreadTime/iterations, 4)} seconds")


app = tk.CTk()
app.geometry("800x600")
app.resizable(False, False)
app.title("Multi-threaded Speed Calculator")

app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=1)
app.columnconfigure(2, weight=1)
app.columnconfigure(3, weight=1)
app.columnconfigure(4, weight=1)
app.columnconfigure(5, weight=1)
app.columnconfigure(6, weight=1)



welcomeLabel = tk.CTkLabel(app, text="Welcome to the multi-threaded speed calculator!")
welcomeLabel.configure(font=("Arial", 24), pady=15)
welcomeLabel.grid(row=0, column=0, columnspan=2)

labelNumEntry = tk.CTkLabel(app, text="Enter a number to calculate the prime numbers up to:")
labelNumEntry.configure(font=("Arial", 20))
labelNumEntry.grid(row=1, column=0)

numberEntry = tk.CTkEntry(app, font=("Arial", 20), width=200)
numberEntry.grid(row=1, column=1)

labelThreadEntry = tk.CTkLabel(app, text=f"Enter number of threads (max ={maxThreads}):")
labelThreadEntry.configure(font=("Arial", 20))
labelThreadEntry.grid(row=2, column=0, pady=5)

threadEntry = tk.CTkEntry(app, font=("Arial", 20), width=200)
threadEntry.grid(row=2, column=1, pady=5)

labelIterationEntry = tk.CTkLabel(app, text=f"Enter number of iterations:")
labelIterationEntry.configure(font=("Arial", 20))
labelIterationEntry.grid(row=3, column=0, pady=2)

iterationEntry = tk.CTkEntry(app, font=("Arial", 20), width=200)
iterationEntry.grid(row=3, column=1, pady=2)

button = tk.CTkButton(app, text="Calculate", font=("Arial", 20), command=calculate)
button.grid(row=4, column=0, pady=2)

resultLabel = tk.CTkLabel(app, text="Results will be displayed here.")
resultLabel.configure(font=("Arial", 20))
resultLabel.grid(row=5, column=0, columnspan=2)

cpuUsageLabel = tk.CTkLabel(app, text="test")
cpuUsageLabel.configure(font=("Arial", 20))
cpuUsageLabel.grid(row=6, column=0, columnspan=2)

app.mainloop()