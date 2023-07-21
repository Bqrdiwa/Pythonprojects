import random
import csv
import time
from tkinter import *
from bs4 import BeautifulSoup
import requests
from barname import *
import jdatetime
import re
from PIL import Image,ImageTk
from tkinter import messagebox
import PIL as pillow
import cv2
import os
import webbrowser
from get_Char import GetChar
from  tkPDFViewer import tkPDFViewer as pdf
from tkinter import filedialog as fd
import mysql.connector
perm = True

g_list = {}

def checker(user,password):
    global g_list
    global perm
    if user != '@example' and password != '':
        for usern in g_list.keys():
            if usern ==  user and g_list[usern][0] == password:
                root_authenticate.destroy()
                perm = True
def save_info(user,password):
    global mcurs
    global conector
    global perm
    if user != '@example' and password != '':
        id = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))
        mcurs.execute('insert into users(username,password,id) values (\'%s\',\'%s\',\'%s\');'%(user.strip(),password.strip(),id))
        conector.commit()
        root_authenticate.destroy()
        perm = True
def animate(ent):
    ent.delete(0,END)
    ent['fg'] = 'black'
    ent.unbind('<FocusIn>')
def login():

    global cnv
    cnv.delete('all')
    tex = ''
    image_login = ImageTk.PhotoImage(Image.open('C:\\Users\BrGaMeRxD\Desktop\Python\\barname_haftegi\Assets\Autenticate_assests\login-rounded-right.png'))
    cnv.image = image_login
    f = ('Consolas',12)
    cnv.create_image((-20,-30),anchor = 'nw',image = image_login)
    ent_user = Entry(bg= '#67D8A1',width =20,font=f,fg='#36514F')
    ent_user.insert(0,'@example')
    ent_user.bind('<FocusIn>',lambda event:animate(ent_user))
    ent_pass = Entry(bg='#67D8A1', width=20, font=f,fg='#36514F')
    ent_pass.bind('<FocusIn>', lambda event: animate(ent_pass))
    cnv.create_text((15,118),text = 'Username:',font=('Poppins',8),anchor ='nw')
    cnv.create_text((15, 175), text='Password:', font=('Poppins', 8), anchor='sw')
    cnv.create_window((20, 170), window=ent_pass, anchor='nw')
    cnv.create_window((20,155),window = ent_user,anchor = 'sw')
    login_imag = ImageTk.PhotoImage(Image.open('C:\\Users\BrGaMeRxD\Desktop\Python\\barname_haftegi\Assets\Autenticate_assests\login_button.png'))
    cnv.Image = login_imag
    cnv.create_image((305,205),anchor='se',image =login_imag)
    button_login= Button(text = 'Login ->',font=('Poppins', 9,'bold'),bg= '#c7ede6',activebackground = '#c7ede6',bd = 0,command=lambda :checker(ent_user.get().strip(),ent_pass.get().strip()))
    cnv.create_window((304,197),window= button_login,anchor='se')
    b_button = Button(text = '<- Back',font=('Poppins', 9,'bold'),bg= '#67D8A1',activebackground = '#67D8A1',bd = 0,command=lambda :authenticate())
    cnv.create_window((300,8),anchor ='ne',window=b_button)
def register():
    global cnv
    f = ('Consolas',12)
    cnv.delete('all')
    image_register = ImageTk.PhotoImage(Image.open('C:\\Users\BrGaMeRxD\Desktop\Python\\barname_haftegi\Assets\Autenticate_assests\\register-rounded-right.png'))
    cnv.image = image_register
    cnv.create_image((-20,-30),anchor = 'nw',image = image_register)
    ent_user = Entry(bg='#67D8A1', width=20, font=f, fg='#36514F')
    ent_user.insert(0, '@example')
    ent_user.bind('<FocusIn>', lambda event: animate(ent_user))
    ent_pass = Entry(bg='#67D8A1', width=20, font=f, fg='#36514F')
    ent_pass.bind('<FocusIn>', lambda event: animate(ent_pass))
    cnv.create_text((15, 118), text='Username:', font=('Poppins', 8), anchor='nw')
    cnv.create_text((15, 175), text='Password:', font=('Poppins', 8), anchor='sw')
    cnv.create_window((20, 170), window=ent_pass, anchor='nw')
    cnv.create_window((20, 155), window=ent_user, anchor='sw')
    register_imag = ImageTk.PhotoImage(
        Image.open('C:\\Users\BrGaMeRxD\Desktop\Python\\barname_haftegi\Assets\Autenticate_assests\\register_button.png'))
    cnv.Image = register_imag
    cnv.create_image((305,205),anchor='se',image =register_imag)
    b_button = Button(text='<- Back', font=('Poppins', 9, 'bold'), bg='#67D8A1', activebackground='#67D8A1', bd=0,
                      command=lambda: authenticate())
    cnv.create_window((300, 8), anchor='ne', window=b_button)
    button_register = Button(text='Register', font=('Poppins', 7, 'bold'), bg='#fce0a2', activebackground='#fce0a2', bd=0,
                          command=lambda: save_info(ent_user.get(), ent_pass.get()))
    cnv.create_window((303, 180), window=button_register, anchor='se')



def authenticate():
    global cnv
    cnv.delete('all')
    cnv.create_image((150, 60), image=image)
    butto1 = Button(text = 'Login',font=('Poppins',' 18'),bd = 0 ,bg= '#67D8A1',
    activebackground ='#67D8A1',command=lambda :login())
    butto2 = Button(text = 'Register',font=('Poppins',' 18'),bd = 0 ,bg= '#67D8A1',
    activebackground ='#67D8A1',command=lambda :register())
    cnv.create_window((133,120),window=butto1,anchor = 'ne')
    cnv.create_window((133,120),window=butto2,anchor = 'nw')

if perm:
    pop_index = 2
    index_saved_d = 99
    text1 = 'password12353bardia neg bahye are baba ghavi bash'
    root = Tk()
    root.title('Barname_Haftegi!!')
    icon_imgage = ImageTk.PhotoImage(Image.open('icon.jpg'))
    root.iconphoto(False,icon_imgage)
    list_items = []
    canvas = Canvas(root,width=900,heigh = 500)
    canvas.pack(anchor ='nw',expand='yes')
    canvas.configure(background='#e1ffb1')
    setting_lable = LabelFrame(canvas,width = 200,bg= 'black',borderwidth= 0)
    canvas.create_window((400, 402), anchor='nw', window=setting_lable)

    frame = Canvas(canvas,width =600,heigh = 320,bg = '#aed581')
    frame.pack(pady = 80,padx = 200,anchor = 'n',expand='yes')
    frame_mode = None
    def change_error(button,text,color,type):
        if not type:
            button['text'] = text
            button['bg']=color
        else:
            button['text'] = text
            button['bg'] = color
            if color == '#8EBADE':
                button['fg']='red'
            else:
                button['fg']='black'
    class Button_Tk():
        def __init__(self,pos,window,text,list):
            self.day = int(jdatetime.datetime.now().strftime('%d'))-1
            self.index = int(text)
            self.text = text+1
            if list[self.index] == 'True':self.color='#02780E'
            elif list[self.index] == 'None':self.color = '#DAC9A1'
            else: self.color = '#B11919'
            self.button_self = Button(window, text=str(text), bg=self.color, width=8, fg='black', activebackground='#A2C4BD',
                                      borderwidth=1, font=('Segoe Print', 10, 'bold'), relief=SUNKEN,highlightthickness=2)
            if  int(self.day) >= text >= int(self.day)-1:
                self.button_self.bind('<Enter>',lambda event:change_error(self.button_self,self.text,'#8EBADE',True))
                self.button_self.bind('<Leave>', lambda event: change_error(self.button_self,self.text,self.color,True))
                self.button_self.bind('<Button-1>',lambda event:self.write_day(True,self.index))
                self.button_self.bind('<Button-2>', lambda event: self.write_day('None',self.index))
                self.button_self.bind('<Button-3>', lambda event: self.write_day(False,self.index))
            else:
                self.button_self.bind('<Enter>', lambda event: change_error(self.button_self, 'No','#8EBADE',False))
                self.button_self.bind('<Leave>', lambda event: change_error(self.button_self, self.text,self.color,False))
            self.button_self.grid(row=pos[0],column=pos[1])
        def write_day(self,mode,index):
            self.list_items = []
            with open('calendar.csv','r') as r:
                reader = csv.reader(r)
                for item in reader:
                    self.list_items.append(item)
            self.list_items[0][index] = mode
            with open('calendar.csv','w',newline='') as w:
                writer = csv.writer(w)
                writer.writerow(item)
            self.update()
        def update(self):
            if self.list_items[0][self.index] == True: self.color='#02780E'
            elif self.list_items[0][self.index] == 'None': self.color = '#DAC9A1'
            else: self.color = '#B11919'
    class rn_Button():
        def __init__(self,value,pos,type,dars,index):
            if type == 'delete':
                self.button = Button(image=value,anchor='nw',font=('Sora',10,'bold'), bg='#aed581', activebackground='#aed581',borderwidth=0)
                self.button.bind('<Button-1>', lambda event: writenotes(dars, index, '','delete'))
            if type == 'edit':
                self.button = Button(text=value, anchor='nw', font=('Sora', 9, 'bold'), bg='#aed581', activebackground='#aed581',borderwidth=0)
                self.button.bind('<Button-1>', lambda event: edit(index, (450, 58), dars))
            frame.create_window(pos,window=self.button)
    class ns_Button():
        def __init__(self,pos,text):
            self.pos = pos
            self.text = text
            self.button = Button(frame,text=self.text,fg='black',font=('Arial',20,'bold'),
                                 bg='#aed581',activebackground='#aed581',borderwidth=0,command=lambda :readnotes(text))
            self.button.bind('<Enter>', lambda event: give_red(self.button,'ok'))
            self.button.bind('<Leave>', lambda event: give_red(self.button, 'ok'))
            frame.create_window(pos,window=self.button)
    class l_Button():
        def __init__(self,text,command,frame,col,row,max_width):
            if command == 'Translate':
                self.button = Button(frame,text = text,fg='black',font=('Consalos',18),width=max_width,bg='#aed581',borderwidth=0,activebackground='#aed581',command =lambda :translat())
            else:
                self.button = Button(frame, text=text,fg='black', font=('Consalos', 18), bg='#aed581',width = max_width, borderwidth=0,activebackground='#aed581', command=lambda: show_learning(command))
            self.button.bind('<Enter>', lambda event: give_red(self.button,'no'))
            self.button.bind('<Leave>', lambda event: give_red(self.button,'no'))
            print(self.button.winfo_reqwidth())
            self.button.grid(row = row, column = col)
    def More_Option(b1,b2,b3,b4):
        b1.grid(row=0,column=0)
        b2.grid(row=1, column=0)
        b3.grid(row=0, column=1)
        b4.grid(row=1, column=1)
    class show_schedule:
        global canvas
        global frame
        def __init__(self,barname,rooz,cordinate):
            self.barname = barname
            self.rooz = rooz
            self.butt = Button(canvas, font=('Arial', 10), width=20, heigh=3, text=rooz, bg='#7da453', borderwidth=0,
               activebackground='#558b2f', command=lambda: self.write())
            canvas.create_window((7,cordinate),window= self.butt,anchor = 'nw')
        def write(self):
            frame.delete('all')
            frame.create_text((10,10),text=self.rooz + ' ---',anchor='nw',font=('Sora',30))
            column = 0
            row = 0
            show_frame = LabelFrame(bd = 1,font=('Sora', 22),height = 210 ,width = 400,text = 'Barname',bg= '#aed581',highlightbackground='#7da453')
            frame.create_window((40,80),window=show_frame,anchor = 'nw')
            for i in self.barname.keys():

                textt = Label(show_frame,text = i + ' --- ' + self.barname[i], font=('Sora', 13),anchor = 'nw',bg= '#aed581')
                textt.grid(row = row,column= column,sticky = 'W')
                row +=1
                if row  == 7:
                    column +=1
                    row = 0
    def writenotes(dars,index,text,type):
        global frame_mode
        global text1
        lessons_list = []
        with open('notes.csv','r',newline='') as r:
            reader = csv.reader(r)
            for row in reader:
                if row[0] == dars:
                    row[index] = text
                lessons_list.append(row)
        with open('notes.csv','w',newline='')as w:
            write = csv.writer(w)
            for row in lessons_list:
                write.writerow(row)
        readnotes(dars)
    def edit(index,pos,dars):
        global frame_mode
        global list_items

        if list_items:
            for item in list_items:
                frame.delete(item)
        entry= Entry(width=20,font=('Sora',15),borderwidth = 0,	selectborderwidth=0,selectbackground='#CAD6B4',bg='#CAD6B4')
        entry.focus()
        edit_button1 = Button(frame,text = 'Edit',font=('Sora',14),fg = 'black',bg='#aed581',activebackground='#aed581',anchor = 'nw',borderwidth=0,command=lambda :writenotes(dars,index,entry.get(),'edit'))
        text =frame.create_text((16,index*50+20),text='-',fill='black',font=('Sora',22),anchor = 'nw')
        entry.bind('<Return>',lambda event:writenotes(dars,index,entry.get(),'edit'))
        frame.create_window((320,60), window=edit_button1)
        frame.create_window(pos,window=entry)
        list_items.append(text)
    def readnotes(dars):
        global frame_mode
        global frame

        frame_mode = None
        frame.delete('all')
        frame.create_text((10,10),text=dars+': ',anchor='nw',font=('Sora',30))
        first_y =78

        e_y_d= 88
        e_y_e= 88
        delete_image= ImageTk.PhotoImage(Image.open('delete.png'))
        frame.image = delete_image
        for i in range(1,11):
            if i <= 5:
                rn_Button('E', (520, e_y_e), 'edit', dars,i)
                e_y_e += 50
            else:
                rn_Button(delete_image, (550, e_y_d), 'delete', dars,i - 5)
                e_y_d += 50
        with open('notes.csv','r') as rea:
            reader = csv.reader(rea)
            for line in reader:
                if line[0] == dars:
                    for item in line:
                        if not item == dars:
                            frame.create_text((30, first_y), text=item, anchor='nw', font=('Arial', 15))
                            frame.create_line(30, first_y+22, 570, first_y+22, width=3)
                            first_y+=50
    def give_red(button,big):
        font_text=button['font']
        color_fg =button['fg']

        font_size = int((re.findall(r'\d+',font_text))[0])
        if re.findall('bold',font_text) != []:
            font_mode='bold'
        else:
            font_mode=''
        if color_fg == 'black':
            button['fg']='red'
            button['bg'] = '#9FA471'
            if big == 'ok':
                button['font']=('Arial', font_size+5, font_mode)
        if color_fg == 'red':
            button['fg']='black'
            button['bg'] = '#aed581'
            if big == 'ok':
                button['font']=('Arial', font_size-5, font_mode)
    def notes_set():
        global frame_mode


        if frame_mode != 'notes_category':
            frame.delete('all')
            root.unbind('r')
            frame.create_text((30,20),text='Ekhtesasi:',font=('Arial', 25, 'bold'),anchor='nw')
            frame.create_text((330, 20), text='Omomi:', font=('Arial', 25, 'bold'), anchor='nw')
            list_darses = [None,'Riazi','Fizik','Shimi','Hendese','Adabiat','Arabi','Dini','Zaban']
            POS_X = 100
            POS_Y = 100
            for i in range(1,9):
                if i <= 4:
                    ns_Button((180,POS_X),list_darses[i])
                    POS_X += 60
                else:
                    ns_Button((450,POS_Y),list_darses[i])
                    POS_Y += 60
            frame_mode = 'notes_category'
    class rightBar:
        def __init__(self):
            canvas.create_text((820, 100), font=('Hahmlet', 15, 'bold'), text='Time_now: ', anchor='nw')
            canvas.create_text((820, 200), font=('Hahmlet', 15, 'bold'), text='Now: ', anchor='nw')
            self.tarikh = canvas.create_text((840, 160), font=('Hahmlet', 15), text=jdatetime.date.today(), anchor='nw')
            self.saat = canvas.create_text((840, 130), font=('Hahmlet', 15), text=(jdatetime.datetime.now().strftime('%H:%M:%S %p')), anchor='nw')
            self.what_is_it = canvas.create_text((840, 230), font=('Hahmlet', 15), text='Loading...', anchor='nw')
        def What_Should_i_Learn(self):
            day = jdatetime.date.today().strftime('%A')
            day_list = [('Saturday',shanbe0),('Sunday',shanbe1),('Monday',shanbe2),('Tuesday',shanbe3),
                        ('Wednesday',shanbe4),('Thursday',shanbe5),('Friday',shanbe6)]
            for rooz,barname in day_list:
                if day == rooz:
                    time_now = float(jdatetime.datetime.now().strftime('%H.%M'))
                    for i in barname.keys():
                        text = re.sub(':','.',i)
                        text = re.split(',',text)
                        if float(text[0]) < time_now < float(text[1]):
                            return barname[i]
        def update(self):
            canvas.delete(self.tarikh)
            canvas.delete(self.saat)
            canvas.delete(self.what_is_it)
            self.tarikh = canvas.create_text((840, 160), font=('Hahmlet', 15), text=jdatetime.date.today(), anchor='nw')
            self.saat = canvas.create_text((840, 130), font=('Hahmlet', 15),
                                           text=(jdatetime.datetime.now().strftime('%H:%M:%S %p')), anchor='nw')
            self.what_is_it = canvas.create_text((840, 230), font=('Hahmlet', 15), text=self.What_Should_i_Learn(), anchor='nw')
            canvas.after(1000,self.update)
    def chage_text(item,newtext):
        item['text']=newtext
    def Q_A(awnser,javab):
        if str(awnser[0]) == javab:
            show_learning('Jt_test')
        elif len(str(awnser[0])) == len(javab) and awnser[0] != javab:
            frame.delete('all')
            text12 = frame.create_text((100, 150), text='Ghalat -- > Sahih :'+str(awnser[0]), fill='red', font=('Consolas', 28),anchor='nw')
            reload_button_soal_onsor = Button(frame,fg='black', text='Reload', anchor='nw', font=('Consolas', 15), borderwidth=0,bg='#aed581',activebackground='#aed581',command=lambda :show_learning('Jt_test'))
            reload_button_soal_onsor.bind('<Enter>', lambda event: give_red(reload_button_soal_onsor, 'ok'))
            reload_button_soal_onsor.bind('<Leave>', lambda event: give_red(reload_button_soal_onsor, 'ok'))
            frame.create_window((60, 32), window=reload_button_soal_onsor)
    def q_c_t(text,entry):
        global currect_list
        global pop_index
        if currect_list == [] :
            show_learning('Jt_Colomn')
        elif text == currect_list[0]:
            x_pos = 40*pop_index
            if len(currect_list[0]) > 1:
                true_text = currect_list[0][0].upper()+currect_list[0][1]
            else:
                true_text = currect_list[0].upper()
            frame.create_text((40*pop_index,230),text=true_text,fill='dark green',font=('Consolas',20))
            pop_index += 1
            entry.delete(0, END)
            entry.focus()
            currect_list.remove(text)

        elif len(text) == len(currect_list[0]):
            if len(currect_list[0]) > 1:
                true_text = currect_list[0][0].upper()+currect_list[0][1]
            else:
                true_text = currect_list[0].upper()
            frame.create_text((40*pop_index,230),text=true_text,fill='dark red',font=('Consolas',20))
            pop_index += 1
            entry.delete(0, END)
            entry.focus()
            currect_list.pop(0)
    class Next_Previous():
        def __init__(self,list= None):
            self.max_index = len(list) -1
            self.in_index = 0
            self.list_item = list
            self.p_mode = 'image'
        def next_page(self):
            if self.p_mode == 'image':
                if not self.in_index == self.max_index:
                    self.in_index += 1
                    self.update_style()
            else:pass
        def previous_page(self):
            if self.p_mode == 'image':
                if not self.in_index == 0:
                    self.in_index -= 1
                    self.update_style()
            else:pass
        def update_keys(self):
            self.b_next = Button(width=3, font=('Segoe UI', 10),activebackground = '#8FB2B2',
                                    text='->', command=self.next_page,bg= '#8FB2B2',fg = 'black',borderwidth = 0)
            self.b_next.bind('<Enter>',lambda event:give_red(self.b_next,'no'))
            self.b_next.bind('<Leave>', lambda event: give_red(self.b_next, 'no'))
            self.b_previous = Button(width=3, font=('Segoe UI', 10),activebackground = '#8FB2B2',
                                    text='<-', command=self.previous_page,bg='#8FB2B2',fg = 'black',borderwidth = 0)
            self.b_previous.bind('<Enter>', lambda event: give_red(self.b_previous, 'no'))
            self.b_previous.bind('<Leave>', lambda event: give_red(self.b_previous, 'no'))
            frame.create_window((2, 322), window=self.b_next, anchor='sw')
            frame.create_window((2, 295), window=self.b_previous, anchor='sw')
        def update_style(self):
            frame.delete('all')
            if self.p_mode == 'image':

                item = ImageTk.PhotoImage(Image.open(self.list_item[self.in_index]))
                frame.image  = item
                self.lable = Label(image = item,borderwidth = 0,width = 600 ,heigh = 320,bg ='#337A7A')
                frame.create_window((2,2),window = self.lable , anchor = 'nw')
                self.update_keys()
    def show_learning(show_item):
        global frame_mode
        global currect_list
        global pop_index
        global setting_lable
        global v2
        global v1

        if show_item == 'jadval_tanavobi':
            frame.delete('all')
            images = GetChar(r'C:\Users\BrGaMeRxD\Desktop\Python\barname_haftegi\Assets\Mandalioft_Table')
            Object = Next_Previous(list=images)
            Object.update_keys()
            Object.update_style()
        if show_item == 'Jt_test':
            frame.delete('all')
            name=give_random_Onsor()
            frame.create_text((200,150),text=name[0]+' :',font=('Arial',50))
            frame.create_text((220, 220), text=name[1][1], font=('Arial', 45),anchor='ne')
            root.bind('r',lambda event:show_learning('Jt_test'))
            entry_onsor = Entry(width=2,font=('Sora',50),borderwidth = 0,	selectborderwidth=0,selectbackground='#aed581',bg='#aed581')
            entry_onsor.bind('<KeyRelease>',lambda event:Q_A(name[1],entry_onsor.get()))
            entry_onsor.focus()
            frame.create_window((400,150),window=entry_onsor)

        if show_item == 'Jt_Colomn':
            frame.delete('all')
            name= give_random_column()
            currect_list = name[1]
            pop_index=2
            frame.create_text((35,30),font=('Consolas',17),text=name[0],anchor='nw')
            coloumn_test = Entry(width=30, font=('Segoe UI', 22), borderwidth=0, bg='#C1F5B1')
            coloumn_test.bind('<KeyRelease>',lambda event:q_c_t(coloumn_test.get().lower(),coloumn_test))
            coloumn_test.focus()
            frame.create_window((56, 70), window=coloumn_test, anchor='nw')

        if show_item == 'Jadval_Tanavobi_Full':
            image_kamel = cv2.imread(r"J_T_K.jpg")
            cv2.imshow('Jadval Tanavobi Kalme',image_kamel)
        if show_item == 'Plan_M':
            frame.delete('all')
            image_plan = ImageTk.PhotoImage(Image.open("barname_madrese.png"))
            frame.image = image_plan
            frame.create_image((2,3),anchor = 'nw',image= image_plan)
            cv2.waitKey(0)
            cv2.destroyAllWindows()




        frame_mode = 'None'
    def entry_focus(entry12,type):
        if type:
            entry12.delete(0,END)
            entry12.configure(bg='#BAE18D')
        if not type:
            entry12.delete(0,END)
            entry12.insert(0,'Search')
            entry12.configure(bg='#aed581')
    def search_meaning(sents,box):
        global frame_mode
        frame.delete('all')
        frame_mode = 'None'
        translat()
        r=requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/'+sents)
        print(r.status_code)
        if 'No Definitions Found' in str(r.json()):
            frame.create_text((33, 125), anchor='nw', text='Word Not Found Make Sure You Wrote That Correctly ! ', font=('Segoe UI', 16,'bold'),fill='red')
        else:
            kolesh = r.json()[0]
            word= kolesh['word']
            phonetic = kolesh['phonetic']
            audio = kolesh['phonetics'][0]['audio']
            meanning_type = kolesh['meanings'][0]['partOfSpeech']
            usage =  kolesh['meanings'][0]['definitions'][0]['definition']
            mean_box = Message(frame,text='Usage:    '+usage, font=('Segoe UI', 16),width=500,anchor='nw',bg='#aed581')
            frame.create_text((30,60),anchor='nw',text='Word:    '+word,font=('Segoe UI',20,'bold'))
            frame.create_text((55, 100), anchor='nw', text='Phonetic:    '+phonetic, font=('Segoe UI', 16))
            frame.create_text((55, 130), anchor='nw', text='PartOfSpeech:    ' + meanning_type, font=('Segoe UI', 16))
            frame.create_window((41,160),window=mean_box,anchor='nw')

            if 'example' in kolesh['meanings'][0]['definitions'][0].keys():
                example_box= Message(frame,text='Example:    '+kolesh['meanings'][0]['definitions'][0]['example'], font=('Segoe UI', 16),width=500,anchor='nw',bg='#aed581')
                y_box=160+mean_box.winfo_reqheight()
                frame.create_window((41,y_box),window=example_box,anchor='nw')
    def translat():
        global frame_mode
        if frame_mode != 'Translate':
            root.unbind('r')
            frame.delete('all')
            searchbox = Entry(width=15,borderwidth=0,bg='#aed581',font=('Segoe Print',18,'bold'))
            searchbox.bind('<FocusIn>',lambda event:entry_focus(searchbox,True))
            searchbox.bind('<FocusOut>', lambda event: entry_focus(searchbox, False))
            searchbox.bind('<Return>',lambda event:search_meaning(searchbox.get(),searchbox))
            frame.create_window((20,10),window=searchbox,anchor='nw')
            searchbox.insert(0, 'Search Word')
            frame_mode= 'Translate'
    def learn():
        global frame_mode
        if frame_mode != 'learn':
            # Shimi
            root.unbind('r')
            frame.delete('all')
            lable_frame= LabelFrame(text='Learn List',bg='#aed581', height= 280,width = 560,font=('Segoe Print',18))
            frame.create_window((20,20),window=lable_frame,anchor='nw')

            learn_list = [('Shimi','jadval_tanavobi'),('Fizik','fiziik')
                ,('Riazi','riazii'),('Hendese', 'hendesee')
                ,('J_T_Full.png', 'Jadval_Tanavobi_Full')
                ,('JT_Q', 'Jt_test'),('Translator', 'Translate'),('JT_Column.Q', 'Jt_Colomn'),('Plan_School', 'Plan_M')]
            # lengher = {}
            # max = 0
            # for index,dars in enumerate(learn_list):
            #     l_dars = len(dars[0])
            #     if l_dars > max:
            #         max = l_dars
            #     lengher[str(l_dars)] = index
            # maximom = learn_list[lengher[str(max)]][0]
            # max_width =  Button( text=maximom,fg='black', font=('Consalos', 18), bg='#aed581', borderwidth=0,activebackground='#aed581').winfo_reqwidth()
            row = 0
            column = 1
            for index,buttonc in enumerate(learn_list):
                l_Button(buttonc[0],buttonc[1],lable_frame,column,row,0)
                row += 1
                if row > 4:
                    row = 0
                    column+=1

            frame_mode = 'learn'
    def menu_animation(button,type):
        if type:
            frame.configure(bg='#58D68D')
            button['bg'] = '#58D68D'
        if not type:
            frame.configure(bg='#aed581')
            button['bg'] = '#aed581'
    def calendar_reset():
        ask_q12 = messagebox.askquestion(title='Reset_Q',message='Do you want to reset your calendar?')
        if ask_q12 == 'yes':
            list_empty=[]
            for i in range(31):
                list_empty.append('None')
            with open('calendar.csv','w',newline='') as w:
                writer = csv.writer(w)
                writer.writerow(list_empty)
            calendar()
    def calendar():
        global frame_mode
        frame_mode = None
        frame.delete('all')
        frame.create_rectangle(25, 25, 585, 305, width=2)
        butoon_reset = Button(text='Reset This Month',font=('Arial',7),borderwidth=0,bg='#3FE181',activebackground='red',command=calendar_reset)
        frame.create_window((600,4),window=butoon_reset,anchor='ne')
        cal_frame =LabelFrame(text='Month: ',font=('Arial',16,'bold'),width = 510,heigh=240,bg='#aed581',borderwidth=0)
        frame.create_window((50, 50), window=cal_frame, anchor='nw')
        list_cal = []
        with open('calendar.csv','r') as r:
            reader = csv.reader(r)
            for i in reader:
                list_cal.append(i)

        row = 3
        col = 7
        for i in range(0,31):
            Button_Tk((row,col),cal_frame,i,list_cal[0])
            if i % 7 == 0:
                col = 0
            if col == 0:
                row += 1
            col += 1
    def home_page():
        global frame_mode
        global profile_image
        global calendar_image

        if frame_mode != 'home_page':
            frame.delete('all')
            frame.create_image((50,45),image=profile_image,anchor='nw')
            header_x=140
            frame.create_rectangle(25,25,585,305,width=2)
            frame.create_line(165, header_x, 560, header_x, width=2)
            frame.create_text((165,header_x+2),text='Name =bardia rajabi(SelfLogo)',font=('Segoe Print',12,'bold'),anchor='sw')
            frame.create_line(165, header_x+40, 560, header_x+40, width=2)
            frame.create_text((165, header_x + 42), text='i belive in that day that is coming soon...', font=('Segoe Print', 8), anchor='sw')
            frame.create_text((165, header_x + 82),text='that day that im sitting and watching my rank in the scoreboard.',font=('Segoe Print', 8), anchor='sw')
            frame.create_text((165, header_x + 122),text=' that it\'s something about 1 or 2  :)',font=('Segoe Print', 8), anchor='sw')
            frame.create_line(165, header_x+80, 560, header_x+80, width=2)
            frame.create_line(165, header_x+120, 560, header_x+120, width=2)
            button_calendar= Button(frame, borderwidth=0, activebackground='#aed581', bg='#aed581',image=calendar_image,command=calendar)
            frame.create_window((50,190),window=button_calendar,anchor='nw')
            frame_mode='home_page'
    class lv_Button():
        def __init__(self,text,pos):
            self.button = Button(frame,text=text,width= 10
                                 ,font=('Segoe UI',16),borderwidth =0 ,bg='#aed581',fg='black'
                                 ,activebackground='#aed581',command=lambda :self.open_link(text))
            self.button.bind('<Enter>',lambda event:give_red(self.button,'yes'))
            self.button.bind('<Leave>',lambda event:give_red(self.button,'yes'))
            frame.create_window(pos,window=self.button,anchor= 'nw')
        def open_link(self,link):
            if link == 'Hendese': id = 137
            if link == 'Dini' :id =213
            if link == 'Riazi': id = 968
            if link == 'Fizik': id = 584
            if link == 'Adabiat': id = 961
            if link == 'Arabi': id = 952
            if link == 'Shimi': id = 172
            webbrowser.open('https://alaatv.com/set/%s'%id)
    def Learning_video():
        global frame_mode

        if frame_mode != 'LV':
            frame.delete('all')
            lv_Button('Riazi', (10, 30))
            lv_Button('Hendese', (270, 66))
            lv_Button('Fizik', (140, 230))
            lv_Button('Shimi', (460, 100))
            lv_Button('Adabiat', (98, 120))
            lv_Button('Dini', (120, 34))
            lv_Button('Arabi', (340, 120))


            frame_mode= 'LV'

    heith = 15
    list_roozha = [(shanbe0,'Shanbe'),(shanbe1,'Yek Shanbe'),(shanbe2,'Do Shanbe'),(shanbe3,'Se Shanbe'),(shanbe4,'Char Shanbe'),(shanbe5,'PangShanbe'),(shanbe6,'Jome')]
    for inde in list_roozha:
        show_schedule(inde[0], inde[1],heith)
        heith += 60
    quotess = len(qouats_sents)
    sents =qouats_sents[random.randint(0,26)]
    sents = sents.replace('.', ' ')
    sents = sents.replace('،', ' ')
    sents = sents.replace('؛', ' ')
    sents.replace('!', ' ')
    if '|' in sents:
        splited = sents.split('|')
        jomle1 = len(splited[0])
        jomle2 = len(splited[1])
        font_size = 15
        if jomle1 >83 or jomle2 > 83:
            font_size = 13
        canvas.create_text((800,20),text = splited[0], font=('Hahmlet', font_size),anchor = 'ne')
        canvas.create_text((780, 50), text=splited[1], font=('Hahmlet', font_size), anchor='ne')
    else:
        canvas.create_text((800, 30), text=sents, font=('Hahmlet', 16), anchor='ne')
    school_image = ImageTk.PhotoImage(Image.open('book.jpg'))
    learn_button = Button(canvas,image = school_image,borderwidth = 0,command=learn)
    canvas.create_window((850,410),window=learn_button)
    notes_image = ImageTk.PhotoImage(Image.open('notes.png'))
    notes_button = Button(canvas,image=notes_image,borderwidth = 0,command=notes_set)
    canvas.create_window((940,410),window = notes_button)
    menu_image = ImageTk.PhotoImage(Image.open('menu.png'))
    menu_lable = Button(image=menu_image, borderwidth=0, activebackground='#58D68D', bg='#aed581', relief=SUNKEN)
    menu_lable.bind('<Enter>', lambda event: menu_animation(menu_lable, True))
    menu_lable.bind('<Leave>', lambda event: menu_animation(menu_lable, False))
    image_menu = frame.create_window((140, 14), window=menu_lable, anchor='nw')
    home__pb = Button(text='Profile',borderwidth=0,fg='black',bg='#e1ffb1',activebackground='#e1ffb1',font=('Consolas',18), relief=SUNKEN,command=home_page)
    home__pb.bind('<Enter>',lambda event:give_red(home__pb,'False'))
    home__pb.bind('<Leave>',lambda event:give_red(home__pb,'False'))
    profile_image=ImageTk.PhotoImage(Image.open('profile.png'))
    calendar_image = ImageTk.PhotoImage(Image.open('Calendar.png'))
    canvas.create_window((1000,2),window=home__pb,anchor='ne')
    # Schedule video
    video_schedule = r"C:\\Users\BrGaMeRxD\Desktop\Python\barname_haftegi\Schedule.mp4"
    button_video = Button(canvas,width=20,heigh=2,font=('Arial',10),text = 'Schedule-Video',borderwidth=0,bg='#81D4D5',command=lambda :os.startfile(video_schedule))
    canvas.create_window((7,440),anchor = 'nw',window = button_video)
    ala_button = Button(canvas, text='LerVideo', borderwidth = 0,width=20,heigh=2 ,font=('Arial',10),bg='#81D4D5',command=Learning_video)
    canvas.create_window((180,440),anchor = 'nw',window = ala_button)
    R_Bar = rightBar()
    R_Bar.update()
    root.resizable(False,False)
    root.mainloop()
