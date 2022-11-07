from tkinter import *
from time import *



window = Tk()

time_label = Label(window, font=("Arial", 50), fg="sky blue", bg="black")
time_label.pack()

day_label = Label(window, font=("Calibri", 25), fg="black")
day_label.pack()

date_label = Label(window, font=("Calibri", 20), fg="black")
date_label.pack()

def update ():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d %Y")
    date_label.config(text=date_string)

    window.after(1000, update)

update ()

window.mainloop()
