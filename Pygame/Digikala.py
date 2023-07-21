import tkinter.messagebox
import requests
import bs4
from tkinter import *
from PIL import ImageTk, Image
import re
def esc(event):
    w1=tkinter.messagebox.askquestion(message='You want to exit?       ')
    if w1 =='yes':
        quit()
def listtextblack(event):
    buttonlist['fg']='black'
def listtextred(event):
    buttonlist['fg']='red'
def onetextblack(event):
    oneitembutton['fg']='black'
def onetextred(event):
    oneitembutton['fg']='red'
def printsearch(event):
    global truelist
    global list_price
    global buttonlist
    global oneitembutton
    global link
    list_price=[]
    truelist=[]
    link=[]
    req = requests.get('https://www.digikala.com/search/?q=%s' % (Serch.get()))
    soup=bs4.BeautifulSoup(req.text,'html.parser')
    soup1=soup.findAll('div', attrs={'class':"c-product-box c-promotion-box js-product-box is-plp"})
    for i in range(0,len(soup1)):
        s2 = (re.sub(r'\s+', ' ', (soup1[i].get('data-title-fa'))))
        truelist.append(s2)
        s2= (re.sub(r'\s+', ' ', (soup1[i].get('data-price'))))
        list_price.append(s2)
        soup2 = soup.find('img', attrs={'alt': soup1[i].get('data-title-fa')})
        link.append(soup2.get('src'))
    boxonebutton(truelist[0],list_price[0],link[0])
    buttonlist = Button(canvas, width=3, text='List', font=("Helvetica", '20'), borderwidth=0, bg='#858916', fg='black',
                        activebackground='#858916')
    oneitembutton = Button(canvas, width=3, text='Item', font=("Helvetica", '20'), borderwidth=0, bg='#858916',
                           fg='black', activebackground='#858916')
    buttonlist.bind('<Enter>', listtextred)
    buttonlist.bind('<Button-1>', boxlist1)
    buttonlist.bind('<Leave>', listtextblack)
    oneitembutton.bind('<Enter>', onetextred)
    oneitembutton.bind('<Leave>', onetextblack)
    oneitembutton.bind('<Button-1>', boxonebutton1)
    canvas.create_window(250, 160, window=oneitembutton)
    canvas.create_window(350, 160, window=buttonlist)
def nextitem(event):
    indextrulist=truelist.index(name1)+1
    if indextrulist != (len(truelist)+1):
        boxonebutton(truelist[indextrulist],list_price[indextrulist],link[indextrulist])
    else:
        pass
def undoitem(event):
    indextrulist1 = truelist.index(name1) -1
    if indextrulist1 != -1:
        boxonebutton(truelist[indextrulist1], list_price[indextrulist1], link[indextrulist1])
    else:
        pass
def showimg(event=NONE):
    for i in truelist:
        if (re.findall(i,listbox.get(ANCHOR))) != []:
            frame.delete('all')
            boxlist()
            with open(r'C:\Users\BrGaMeRxD\Desktop\DigikalaItem\Images\Itemimg.png', 'wb') as wr:
                wr.write(requests.get(link[truelist.index(i)]).content)
            p1=Image.open(r'C:\Users\BrGaMeRxD\Desktop\DigikalaItem\Images\Itemimg.png')
            heigh1=400
            width1=int(heigh1/p1.height*p1.width)
            okpic=p1.resize((heigh1,width1),Image.ANTIALIAS)
            p1=ImageTk.PhotoImage(okpic)
            frame.image=p1
            frame.create_rectangle(690, 31, 1300, 562, fill='#7DDC64', outline='')
            frame.create_image(1000, 250, image=p1)
            frame.create_text(1100, 470, text=i, fill='black', font=("Helvetica", '10'))
            frame.create_text(850, 490, text=list_price[truelist.index(i)], font=("Helvetica", '20'))
def boxlist1(event):
    frame.delete('all')
    pwshowimg=ImageTk.PhotoImage(Image.open(r'C:\Users\BrGaMeRxD\Desktop\DigikalaItem\Images\Digikalajifjif.jfif'))
    frame.create_text(1000, 400, text='Select your commodity', font=("Helvetica", '20'))
    frame.image=pwshowimg
    frame.create_image(1000, 250, image=pwshowimg)

    boxlist()
def boxonebutton1(event):
    boxonebutton(truelist[0],list_price[0],link[0])
def boxlist():
    global listbox
    listbox = Listbox(frame, heigh=33, width=100, bg='dark green')
    frame.create_window(330, 296, window=listbox)
    for i in range(len(truelist)):
        listbox.insert(END, truelist[i]+' -price:')
        listbox.itemconfig(END, {'bg': '#6FD99C'})
        listbox.insert(END, list_price[i])
        listbox.itemconfig(END, {'bg': '#6FD99C'})
    listbox.bind('<Button-1>',showimg)


def boxonebutton(name,price,img):
    global name1
    name1=name
    frame.delete('all')
    print(name)
    frame.create_text(650, 450, text=name, font=("Helvetica", "20"),fill='black')
    frame.create_text(650, 500, text=price+'  T  ', font=("Helvetica", "20"),fill='black')
    with open(r'C:\Users\BrGaMeRxD\Desktop\DigikalaItem\Images\Itemimg.png','wb')as w:
        w.write(requests.get(img).content)
    p1=Image.open(r'C:\Users\BrGaMeRxD\Desktop\DigikalaItem\Images\Itemimg.png')
    heigh1=int(400)
    width1=int(heigh1 / p1.height * p1.width)
    okpic=p1.resize((int(heigh1),width1),Image.ANTIALIAS)
    p1=ImageTk.PhotoImage(okpic)
    frame.image=p1
    frame.create_image(650,220,image=p1)
    frame.create_window(1250, 430, window=button2)
    frame.create_window(100,430,window=button3)
root = Tk()
root.geometry('1600x900')
root.title('Digikala')
searchpng=ImageTk.PhotoImage(Image.open(r'C:\Users\BrGaMeRxD\Desktop\DigikalaItem\Images\Searchboxphoto.png'))
searchpngicon = ImageTk.PhotoImage(Image.open(r'C:\Users\BrGaMeRxD\Desktop\DigikalaItem\Images\Search.png'))
nextpng=ImageTk.PhotoImage(Image.open(r'C:\Users\BrGaMeRxD\Desktop\DigikalaItem\Images\Next.png'))
undopng=ImageTk.PhotoImage(Image.open(r'C:\Users\BrGaMeRxD\Desktop\DigikalaItem\Images\Undo.png'))
canvas = Canvas(root,width=1600,heigh=900,bg= 'blue')
canvas.pack()
frame=Canvas(canvas,width=1350,heigh=900,bg='#107669')
root.bind('<Escape>',esc)
button1 = Button(root,width=60,font=("Helvetica", "16"),image=searchpngicon,borderwidth=0)
button1.bind('<Button-1>',printsearch)
canvas.create_window(1500,160,window=button1)
canvas.create_rectangle(0,0,160,1000,fill='#22211F')
canvas.create_rectangle(160,200,1600,0,fill='#858916')
canvas.create_image(1250,160,image=searchpng)
Serch=Entry(canvas,width=40,font=("Helvetica", "16"),bg='#FFFFFF',borderwidth=0)
Serch.bind('<Return>',printsearch)
canvas.create_window(1230,160,window=Serch)
frame.grid(pady=240,padx=200)
button2=Button(frame,width=180,image=nextpng,borderwidth=0,heigh=160)
button3=Button(frame,width=180,image=undopng,borderwidth=0,heigh=160)
button2.bind('<Button-1>',nextitem)
button3.bind('<Button-1>',undoitem)


























root.mainloop()
