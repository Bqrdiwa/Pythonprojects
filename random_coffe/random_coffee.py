from tkinter import *
import requests
from PIL import Image,ImageTk
from io import BytesIO
def reload():
    global pic1
    get_image = requests.get('https://coffee.alexflipnote.dev/random')
    pic = Image.open(BytesIO(get_image.content))
    height = 600
    width = int(height / pic.height * pic.width)
    pic = pic.resize((width, height), Image.ANTIALIAS)
    pic_ok = ImageTk.PhotoImage(pic)
    canvas.image = pic_ok
    canvas.delete('all')
    canvas['width'] = pic.width
    canvas['height'] = pic.height
    pic1 = canvas.create_image((0, 24), image=pic_ok, anchor='nw')
    canvas.create_window((pic.width / 2, 0), window=button1, anchor='n')

root = Tk()
root.title('Coffee')


get_image = requests.get('https://coffee.alexflipnote.dev/random')
pic = Image.open(BytesIO(get_image.content))
height= 600
width = int(height / pic.height * pic.width)
pic = pic.resize((width,height),Image.ANTIALIAS)
pic_ok = ImageTk.PhotoImage(pic)
canvas = Canvas(root,width=pic.width-1,heigh=pic.height-1)
canvas.pack(anchor='nw')
button1 = Button(canvas,width=50,heigh=1,text='Reload',fg = '#000080',bg = '#FA8072',activebackground='#E9967A',borderwidth = 0,command=reload)
pic1 = canvas.create_image((0,24),image=pic_ok,anchor='nw')
canvas.create_window((pic.width/2,0),window=button1,anchor='n')







root.mainloop()