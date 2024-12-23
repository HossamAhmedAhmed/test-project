import tkinter 
from tkinter import *

window=tkinter.Tk()

window.geometry("600x500")

window.title("Form")

window.config(bg="skyblue")

lbl1 =Label(window,text="label1")
lbl1.place(x=0,y=0)

window.mainloop()