#this tool is created by Abhimanyu Sharma
import tkinter as tk #tkinter import
from tkinter import filedialog, Text
import os #os import
root = tk.Tk()
apps = []
#temp apps save
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        print(tempApps)
    tempApps = tempApps.split(',')
    apps = [x for x in tempApps if x.strip()]

#define add app
def addApp():

    for widget in frame.winfo_children():
        widget.destroy()
    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("executables","*.exe"),("all files","*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.label(frame, text=app, bg="gray")
        label.pack()
#define run apps 

def runApps():
    for app in apps:
        os.startfile(app)

    
canvas = tk.Canvas(root, height=500, width= 500, bg="#FF9529") #main GUI interface

canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8,relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10,pady=5, fg="white",bg="#263D42", command=addApp) #open file button

openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10,pady=5, fg="white",bg="#263D42", command=runApps) #run apps button

runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

#starts GUI app   
root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')