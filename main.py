import time
from datetime import datetime
import webbrowser
import tkinter as tk
from tkinter import simpledialog


ROOT = tk.Tk()
ROOT.withdraw()
input= simpledialog.askstring(title = "Join google meets", prompt = "Enter start time in military : ")

lst = [
    ["https://meet.google.com/lookup/dly4m7k3aj?authuser=1&hs=179", input , "8:39"],
]
isStarted = False

for i in lst:
    while True:
        if isStarted == False:
            if datetime.now().hour == int(i[1].split(':')[0]) and datetime.now().minute == int(i[1].split(':')[1]): #check if the time right now equals to time we imputed if so open
                webbrowser.open(i[0])
                isStarted = True
        elif isStarted == True:
            if datetime.now().hour == int(i[2].split(':')[0]) and datetime.now().minute == int(i[2].split(':')[1]):
                time.sleep(1)
                isStarted = False
                break
