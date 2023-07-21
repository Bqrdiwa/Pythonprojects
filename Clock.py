import tkinter.font
from tkinter import *
from time import strftime
root= Tk()
root.title = ('Clock')
def time():
    timestr= strftime('%H:%M:%S %p')
    label.config(text =timestr)
    label.after(1000,time)
label= Label(root,font=('Pygame\Assets\Fonts\clock.TTF',60),foreground='blue',bg='black')
label.pack()
time()














root.mainloop()
