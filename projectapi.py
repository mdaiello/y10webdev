import tkinter as tk
import requests
from tkinter import *
import webbrowser
from os import path


def write_slogan():
    print("Welcome to Tkinter Window. Want to acess my site, please click below")

myrequest = requests.get("https://clinicaltrials.gov/api/query/full_studies?expr=heart+attack&fmt=json")
datajson = myrequest.json()

ofile = open("apiproject.html","w")
ofile.write("<h1>" + datajson['Expression'] + "</h1>")
ofile.close()

print("done")

root = tk.Tk()
root.geometry('400x400')
root.title('Welcome to Tkinter Window. Want to acess my site, please click below')
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Access site",
                   fg="green",
                   command=open("apiproject.hmtl","w")
slogan.pack(side=tk.LEFT)

root.mainloop()
