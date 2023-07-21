from pynput import mouse
import time
from tkinter import *
import random
mouseob = mouse.Controller()
root= Tk()
root.title = 'Auto Clicker'
root.geometry('400x300')
def checking(event):
    if len(click_persec.get()) > 1:
        click_persec.delete(0,END)
def Apply():
    global error1
    if click_persec.get() != '':
        try:int(click_persec.get())
        except:
            error1=canvas.create_text((125,75),text='Please Enter A Number',fill ='red')
        else:
            try:
                canvas.delete(error1)
            except:
                pass
    else:
        return

    while True:
        time.sleep(0.1)
        mouseob.click(mouse.Button.left,100)


canvas =Canvas(root,width=400,height=399,bg='black')

canvas.pack(padx=0,pady=0)
click_persec=Entry(canvas,width=2,textvariable='',font=('Verdana',20))
autoclick_button = Button(canvas,text = 'Autoclick',width = 10,height=2,borderwidth=1,fg = 'blue',font=('Franklin Gothic',10),command= Apply)


click_persec.bind('<Key>',checking)
canvas.create_window((125,40),window=click_persec)
canvas.create_window((50,40),window=autoclick_button)














root.mainloop()
