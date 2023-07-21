import random
from tkinter import *
from Assests.Data import *
from PIL import Image, ImageTk, ImageFilter, ImageEnhance,ImageFile
import mysql.connector
import re
import copy
import tkinter.messagebox
from io import BytesIO
import sys
from tkinter.filedialog import askopenfilename
import ctypes
import pyautogui
import jellyfish
ImageFile.LOAD_TRUNCATED_IMAGES = True
ctypes.windll.shcore.SetProcessDpiAwareness(1)
images = images_mode1
main_surface = Tk()
layer_1 = Canvas(main_surface, width=1000, height=600)
layer_1.pack()
l_c = 0

user_data = ('Bavar',)
username =user_data[0]
conector = mysql.connector.connect(host='136.243.153.26' , username='stikiir_Bardia', password='4nJ2ZuXbJjS0',
                                       database='stikiir_Paradox')
user = conector.cursor()
commend = "select * from Users where username = %s"
user.execute(commend, user_data)
APPS = [
    {'name': 'Jdvl-Tnvbi',
     'id': '0010',
     'icon_dir': 'app_chemestry',
     'xp': '0',
     'description': 'Jdvl-TnVobi',
     'command': 'lesson_chem_jadval',
     },
    {'name': 'Profile-Editor',
     'id': '0001',
     'icon_dir': 'app_editbio',
     'xp': '7',
     'description': 'Profile',
     'command': 'Bio_Editer'},
    {'name': 'Explorer',
     'id': '0002',
     'icon_dir': 'app_searchprofile',
     'xp': '7',
     'description': 'Search',
     'command': 'Search_profile'},

]
# global user_data_khales
# user.fetchall()[0]
user_data = user.fetchall()[0]
mdata_configer = re.split('\|\*\*\|', user_data[3])
data = {
    'username': user_data[0],
    'password': user_data[1],
    'xp': mdata_configer[3],
    'sex': mdata_configer[2],
    'id': mdata_configer[0],
    'bio': re.split('=--=--=', mdata_configer[1]),
    'date_create': mdata_configer[4],
    'profile_image': user_data[2]
}
APP_NAME = []
for i in APPS:
    APP_NAME.append(i['name'])


def back_to_normal(event):
    blur_layer.destroy()
    for i in d_list:
        layer_1.delete(i)
    if event[0] == 'profile':
        profile()
        if event[1] == 'ProfileEditor':
            Profile_Editor()
    elif event[0] == 'learn':
        learn()
        if event[1] == 'Jadval-Tanavobi':
            l_jadval_Tanavobi()
def blur_popup(backtore, Req,Type, button=None, image=None, text=None, link=None):
    # backtore = ((leanr,game,profile),APP)
    # req = ((width , height),color)
    global d_list
    global blur_layer
    if Type == 'Build':
        d_list = []



        x_pos = main_surface.winfo_x() + 11
        y_pos = main_surface.winfo_y() + 33
        ss = pyautogui.screenshot()
        ss = ss.crop((x_pos, y_pos, x_pos + 997, y_pos + 598)).filter(ImageFilter.GaussianBlur(radius=10)).filter(
            ImageFilter.SMOOTH_MORE())
        filter = ImageEnhance.Brightness(ss)
        ss = filter.enhance(0.8)
        ss = ImageTk.PhotoImage(ss)
        blur_layer = Canvas(width=1000, height=600)
        layer_1.create_window((0, 0), anchor='nw', window=blur_layer)
        blur_layer.create_image((2.5, 2.5), image=ss, anchor='nw')
        blur_layer.image = ss
        layer_1.create_window((0, 0), anchor='nw', window=blur_layer)
        blur_layer.bind('<Button-2>', lambda event:back_to_normal(backtore))
        h = Req[0][1] / 2
        x = Req[0][0] / 2
        round_rectangle(500 - x, 300 - h, 500 + x, 300 + h, Req[1], canvas='blur_layer')

    class Show_Notifiction_blur:
        def __init__(self, button=None, image=None, text=None, link=None):

            if button != None:
                # 1 - Coordination 2 - Button text 3 - Button type (rounded,line....) 4 - Button Colors (Text Fill ,
                # Text Animation,if rounded color of red and line color of line , animation_bigsize) 5 - Button text
                # font 6 - Button Command change in Text_with_a in command runner CENTER 7 - Button sqale _rounded

                self.but_cord = button[0]
                self.but_text = button[1]
                self.but_type = button[2]  # rounded button ...
                self.but_color = button[3]
                self.but_font = button[4]
                self.bu_commnad = button[5]
                self.sqale= button[6]
                if self.but_type == 'Rounded':
                    self.button = Text_With_A((self.but_text, self.but_font, self.but_color[0], self.but_color[1]), blur_layer,
                                self.but_cord,
                                self.bu_commnad, self.but_color[3], square=self.but_color[2],canva_name_rounded='blur_layer',sqale=self.sqale)
                elif self.but_type == 'Line':
                    self.button = Text_With_A((self.but_text, self.but_font, self.but_color[0], self.but_color[1]), blur_layer,
                                self.but_cord,
                                self.bu_commnad, self.but_color[3], line=self.but_color[2],canva_name_rounded='blur_layer')
                else:
                    self.button = Text_With_A((self.but_text, self.but_font, self.but_color[0], self.but_color[1]), blur_layer,
                                self.but_cord,
                                self.bu_commnad, self.but_color[3],canva_name_rounded='blur_layer')
                d_list.append(self.but_text)
            if image != None:
                # 1 - Coordinations
                # 2 - image(byte or path)
                # 3 - image tag
                self.cord_img = image[0]
                self.image = image[1]
                self.tag = image[2]
                if type(self.image) == bytearray or type(self.image) == bytes:
                    img = BytesIO(bytes(self.image))
                    ima =Image.open(img).resize((100,100))
                    self.image = ImageTk.PhotoImage(ima)
                    img.close()
                else:
                    self.image = ImageTk.PhotoImage(Image.open(self.image))
                blur_layer.create_image(self.cord_img,anchor='center',image = self.image,tags = self.tag)
            if text != None:
                # cord = text[0]  text = text[1]  font = text[2]  fill= text[3] anchor = text[4]
                blur_layer.create_text(text[0],text=text[1],font = text[2],fill=text[3],anchor=text[4])
        def change(self,Thing):
            if Thing[0]  == 'Image':
                if type(Thing[1]) == bytearray:
                    img = BytesIO(bytes(self.image))
                    ima = Image.open(img).resize((100, 100))
                    self.image = ImageTk.PhotoImage(ima)
                    img.close()
                else:
                    self.image = ImageTk.PhotoImage(Image.open(Thing[1]).resize((100,100)))
                blur_layer.itemconfigure(self.tag,image=self.image)
    return Show_Notifiction_blur(button=button, image=image, link=link, text=text)
def prof_previw(where_u_come, UserDATA):
    # userdata = name+id,profile,bio
    layer_2_wallpaper_C()
    Text_With_A(('Back', ('Poppins', 12), '#A4CDCA', '#7BA29F'), layer_2, (50, 30), 'search_profile', 1,
                square='#EE4E34',sqale=(.9,1.1))
    round_rectangle(40, 55, 280, 250, '#FCEDDA', 'prof')
    img = BytesIO(bytes(UserDATA[1]))
    imag = ImageTk.PhotoImage(Image.open(img))
    img.close()
    layer_2.create_image((60, 75), anchor='nw', image=imag)
    layer_2.imf = imag
    name = UserDATA[0][:-5]
    font_size = 19-len(name)

    round_rectangle(180,60,270,100,'#EE4E34')
    layer_2.create_text((225,80),text = name,font = ('Poppins',font_size))
    layer_2.create_oval(50, 65, 170, 185, width=22, outline='#FCEDDA')
    layer_2.create_oval(60, 75, 160, 175, width=6, outline='#EE4E34')
    row = 180
    bio = re.split('=--=--=', UserDATA[2])
    for i in range(0, 4):
        bio[i] = re.split('\+', bio[i])
    for i in bio:
        if i[0] != 'None' and i[1] != None:
            if i[0] in data:
                layer_2.create_text((55, row),text = '- ' + i[1] + ' -' + data[i[0]],font = ('Poppins', 11,'bold'),fill ='#272626',anchor = 'nw')

            else:
                layer_2.create_text((55, row), text='- ' + i[1] + ' -' + i[0], font=('Poppins', 11,'bold'),
                                    fill='#272626', anchor='nw')
            row += 16

        elif i[0] == 'None' and i[1] != 'None':
            layer_2.create_text((55, row), text='- ' + i[1], font=('Poppins', 11),
                                fill='#272626', anchor='nw')
            row += 16
def ask(type):
    if type == 'image':
        file_path=askopenfilename(title = 'Paradox-Assistant' ,filetypes =[('image files','*.png'),('image files','*.jpg')])
    return  file_path
class Text_With_A:
    def __init__(self, textinfo, canva, Cord, cmd, bigsize, moredata=None, square=None, line=None, bold='normal',
                 anchor='center',canva_name_rounded = 'layer_2',sqale = 'None'):
        # textinfo = text,font,fill,animatefill

        self.text = textinfo[0]
        self.big_a = bigsize
        self.font = (textinfo[1][0], textinfo[1][1], bold)
        self.animate_color = textinfo[3]
        self.color = textinfo[2]
        self.comd = cmd
        self.canv = canva
        self.Bold = bold
        if self.animate_color != None and bigsize != None:
            self.canv.tag_bind(self.text, '<Enter>', lambda event: self.animate(True))
            self.canv.tag_bind(self.text, '<Leave>', lambda event: self.animate(False))
        if square != None:
            snimator = self.font[1]
            if anchor == 'center':
                x_pos = ((snimator * len(self.text))/2)
                if sqale != 'None':
                    x_pos = x_pos*sqale[0]
                    snimator = snimator*sqale[1]
                round_rectangle(Cord[0] - snimator- x_pos, Cord[1] - snimator/2-snimator/1.5, Cord[0] + x_pos+snimator ,
                                Cord[1] + snimator/2+snimator/1.5,
                                square, self.text, canvas=canva_name_rounded)
                self.Object = canva.create_text(Cord, text=self.text,
                                                font=textinfo[1], fill=self.color, tag=self.text, anchor=anchor)
            else:print('cant use req future')
        elif line != None:
            self.Object = canva.create_text(Cord, text=self.text, font=self.font, fill=self.color, tag=self.text,
                                          anchor=anchor)
        else:
            self.Object = canva.create_text(Cord, text=self.text, font=textinfo[1], fill=self.color, tag=self.text,
                                          anchor=anchor)
        if moredata != None:
            self.canv.tag_bind(self.text, '<Button-1>', lambda event: prof_previw(moredata[0], moredata[1]))

        else:
            self.canv.tag_bind(self.text, '<Button-1>', lambda event: self.cmd(self.comd))
    def animate(self, event):
        if event:
            self.canv.itemconfigure(self.Object, font=(self.font[0], int(self.font[1]) + self.big_a, self.Bold),
                                    fill=self.animate_color)
        else:
            self.canv.itemconfigure(self.Object, font=self.font, fill=self.color)
    def cmd(self, command):
        global page
        if command != None:
            if command == 'search_profile':
                search_profile(event='SeeAgain')
            elif command == 'edit_avatar':
                edit_avatar()
            elif command == 'edit_bio':
                edit_bio()
            elif command[0] == 'Choose_File':

                if command[1] == 'edit_avatar':
                    global Profile_Image
                    path = ask('image')
                    if path != '':
                        Profile_Image.change(('Image',path))
                        self.comd = ('Choose_File','save_img')
                        blur_layer.itemconfigure(self.Object,text='Save',font=('Poppins',16))
                        self.path = path
                elif command[1] == 'save_img':
                    ih = Image.open(self.path)
                    ih= ih.resize((100,100))
                    ig = BytesIO()
                    ih.save(ig, format='PNG', subsampling=0, quality=100,resize=(100,100))
                    data['profile_image'] = ig.getvalue()
                    send_get_data()
                    back_to_normal(('profile','ProfileEditor'))
            elif command == 'p_fixer_T':
                if len(list_users) // 5 + 1 > page + 1:
                    page += 1
                    show(page)
            elif command == 'p_fixer_F':
                 if page - 1 != -1:
                    page -= 1
                    show(page)
            elif command == 'Chem_Jadval_Test':
                # 1 - Coordination 2 - Button text 3 - Button type (rounded,line....) 4 - Button Colors (Text Fill ,
                # Text Animation,if rounded color of red and line color of line , animation_bigsize) 5 - Button text
                # font 6 - Button Command change in Text_with_a in command runner CENTER 7 - Button sqale _rounded
                blur_popup(('learn','Jadval-Tanavobi'),((300,330),'#b5b8cb'),'Build',button=((500,350),'Start',
                           'Rounded',('#2B8BB2','#146079','#98A4A8',4),('Poppins',15),'Chem_start_test',(1.5,2.5)))
                blur_popup(None, None, 'Add',text=((500,170),'Time:  18','Poppins 14','#4B4B4B','center'))
                blur_popup(None, None, 'Add', text=((500, 210), 'Test:  20', 'Poppins 14', '#4B4B4B', 'center'))
                blur_popup(None, None, 'Add', text=((500, 250), 'Jadval-Tanavobi Training', 'Poppins 14', '#4B4B4B', 'center'))
            elif command == 'Chem_start_test':
                back_to_normal(('learn',None))
                

    def destroy(self):
        self.canv.delete(self.text)
def round_rectangle(x1, y1, x2, y2, color, tag='None', canvas='layer_2', r=25, **kwargs):
    points = (
        x1 + r, y1, x1 + r, y1, x2 - r, y1, x2 - r, y1, x2, y1, x2, y1 + r, x2, y1 + r, x2, y2 - r, x2,
        y2 - r, x2, y2, x2 - r, y2, x2 - r, y2, x1 + r, y2, x1 + r, y2, x1, y2, x1, y2 - r, x1, y2 - r,
        x1, y1 + r, x1, y1 + r, x1, y1)
    if canvas == 'layer_2':
        layer_2.create_polygon(points, **kwargs, smooth=True, tags=tag, fill=color)
    elif canvas == 'blur_layer':
        blur_layer.create_polygon(points, **kwargs, smooth=True, tags=tag, fill=color)
def edit_bio():
    global delete_list
    global d_l
    global page

    layer_2_wallpaper_C()
    delete_list = []
    page = 0
    d_l = []

    class Buttons:
        def __init__(self, Cord, text, canva, font, fill, animate_color, big_size, line_color):
            self.tag = text
            self.ctc = (fill, animate_color)
            self.canv = canva
            self.font = font
            self.command = text
            self.big_size = big_size
            self.tex = self.canv.create_text(Cord, text=text, tag=text, font=font, fill=fill, anchor='w')
            self.canv.tag_bind(text, '<Enter>', lambda event: self.animate(True, 1, self.tag, self.ctc))
            self.canv.tag_bind(text, '<Leave>', lambda event: self.animate(False, 1, self.tag, self.ctc))
            self.canv.tag_bind(text, '<Button-1>', lambda event: self.command_runner(self.command))
            if line_color != False:
                layer_2.create_line(Cord[0] - font[1] * 0.5, Cord[1] - font[1], Cord[0] - font[1] * .5,
                                    Cord[1] + font[1], width=int(self.font[1] / 3.2), fill=line_color, tags=text + 'L')

        def animate(self, event, Mode, tag, colortc):
            if Mode == 1:
                if event:
                    self.canv.itemconfigure(self.tag, fill=colortc[1],
                                            font=(self.font[0], self.font[1] + self.big_size))
                else:
                    self.canv.itemconfigure(self.tag, fill=colortc[0], font=self.font)
            elif Mode == 2:
                if event:
                    self.canv.itemconfigure(tag, fill=colortc[1])
                else:
                    self.canv.itemconfigure(tag, fill=colortc[0])

        def command_runner(self, command):
            global APP_NAME
            global T_xp
            global delete_list
            global d_l
            global page
            global data_bio

            for i in d_l:
                i.destroy()
                delete_list.append('>')
                delete_list.append('<')
            for i in delete_list:
                layer_2.delete(i)
            delete_list = []
            if command == 'Done':
                def ask():
                    return tkinter.messagebox.askyesno('Paradox-Gaurd', 'Are you sure abount this perform.')

                if data_bio != data['bio']:
                    if ask():
                        layer_2_wallpaper_C()
                        data['bio'] = data_bio
                        send_get_data()

                else:
                    tkinter.messagebox.showinfo('Paradox-Notif', 'Nothing to Change!')
            elif command == 'Back':
                Bio(data['bio'])
                Profile_Editor()
            elif command == 'Date':
                self.line_checker('date_create', 'Date Create')
            elif command == 'Sex':
                self.line_checker('sex', 'Sex')
            elif command == 'Xp':
                APP_NAME = []
                list_app_xp_true = []
                T_xp = 0

                for i in APPS:
                    xp = i['xp']
                    if xp != None:
                        name = i['name']
                        APP_NAME.append(name)
                        list_app_xp_true.append((name, xp, images[i['icon_dir']]))
                        T_xp += int(xp)

                if len(list_app_xp_true) / 3 <= page:
                    page -= 1
                if page == -1: page += 1
                Buttons((20, 150), '>', layer_2, ('Poppins', 12), '#FFBBB4', '#FA8072', 2, False)
                Buttons((20, 170), '<', layer_2, ('Poppins', 12), '#FFBBB4', '#FA8072', 2, False)

                def page_c(page):
                    r_c = 1
                    y_pos = 150
                    if page == 0:
                        Buttons((70, 150), 'Total-Xp', layer_2, ('Consolas', 13), '#F08080', '#FA8072', 2,
                                '#EF9292')
                        delete_list.append('Total-Xp')
                        delete_list.append('Total-XpL')
                        r_c += 1
                        y_pos = 177
                    x_pos = 92

                    for i in list_app_xp_true[page * 2:]:
                        delete_list.append(i[0])
                        delete_list.append(i[0] + 'L')
                        Buttons((x_pos, y_pos), i[0], layer_2, ('Consolas', 12), '#F08080', '#FA8072', 2, '#EF9292')

                        img = Image.open(i[2])
                        img = img.resize((16, 16), Image.ANTIALIAS)
                        img = ImageTk.PhotoImage(img)
                        Label_img = Label(image=img, width=18, height=18, bd=1, background='#A93226')
                        Label_img.image = img
                        d_l.append(Label_img)
                        layer_2.create_window((82, y_pos), anchor='e', window=Label_img)
                        y_pos += 27
                        r_c += 1
                        if r_c > 3:
                            break

                page_c(page)
            elif command == 'Delete':
                self.line_checker('None', 'None')
            elif command == 'Custom':

                def check_entry(entry_text):
                    if len(entry_text.get()) > 20:
                        entry_text.delete(20, END)
                    layer_2.itemconfigure('mlenght', text=str(len(entry_text.get())) + '/20')
                    self.line_checker('None', entry_text.get())

                def paste():
                    self.line_checker(text, 'None')

                round_rectangle(50, 200, 200, 230, '#FFBBB4', 'entry')
                delete_list.append('entry')
                v = StringVar(layer_2, value='  .-. Type .-.')
                entry_custom = Entry(bd=0, width=15, font=('Consolas', 12), bg='#FFBBB4', textvariable=v, fg='black')
                d_l.append(entry_custom)
                layer_2.create_text((50, 200), text='0/20', anchor='sw', font=('Poppins 12'), fill='#BAA4A2',
                                    tags='mlenght')
                delete_list.append('mlenght')
                entry_custom.bind('<Button-1>', lambda event: entry_custom.delete(0,
                                                                                  END) if entry_custom.get() == '  .-. Type .-.' else None)
                entry_custom.bind('Return', lambda event: paste())
                entry_custom.bind('<KeyPress>', lambda event: check_entry(entry_custom))
                entry_custom.bind('<KeyRelease>', lambda event: check_entry(entry_custom))
                layer_2.create_window((54, 204), anchor='nw', window=entry_custom)

            elif command == '>':
                page += 1
                self.command_runner('Xp')
            elif command == '<':
                page -= 1
                self.command_runner('Xp')
            else:
                for i in APPS:
                    if i['name'] == self.tag:
                        self.line_checker(i['xp'] + ' xP', self.command)
                    elif self.tag == 'Total-Xp':
                        self.line_checker(str(T_xp) + ' XP', 'Total-Xp')

        def line_checker(self, agar, angah):
            def animate_text(Cord, text, font, canvas, color, command, text_Tip):
                global list_color
                list_color = ['#641E16', '#7B241C', '#922B21', '#A93226', '#CD6155', '#D98880', '#F2D7D5']

                def randomc():
                    id_c_t = random.randint(0, 5)
                    id_c = random.randint(0, 5)
                    while id_c == id_c_t: id_c = random.randint(0, 5)
                    c_selected = list_color[id_c]
                    t_selected = list_color[id_c_t]
                    canvas.create_line(Cord[0] - font[1] * 0.5, Cord[1] - 5, Cord[0] - 2, Cord[1] + 1, width=width,
                                       fill=t_selected, tags='Lines')
                    canvas.create_line(Cord[0] - font[1] * 0.5, Cord[1] - font[1], Cord[0] - font[1] * 0.5,
                                       Cord[1] + font[1], width=width, fill=c_selected, tags='Lines')

                width = 4
                randomc()
                canvas.create_text(Cord, text=text, font=font, anchor='w', tag=text, fill='#CD5C5C', tags=text)

                canvas.tag_bind(text, '<Leave>', lambda event: self.animate(False, 2, text, ('#CD5C5C', '#6E2C00')))
                canvas.tag_bind(text, '<Enter>', lambda event: self.animate(True, 2, text, ('#CD5C5C', '#6E2C00')))
                canvas.tag_bind(text, '<Button-1>',
                                lambda event: self.data_changer((command, text_Tip), int(text[-1]), text[-1]))

                delete_list.append(text)
                delete_list.append('Lines')

            options = (angah, agar)
            y_pos = 30
            for i in range(4):
                str_line = 'Line-' + str(i + 1)
                layer_2.delete(str_line)
                animate_text((180, y_pos), str_line, ('Poppins', 16), layer_2, 'black', options[0], options[1])
                y_pos += 40

        def data_changer(self, datatochange, row, line_clicked):
            global data_bio
            global l_c
            l_c = int(line_clicked) - 1
            fake_data = copy.deepcopy(data_bio)
            esmovalue = datatochange[1] + '+' + datatochange[0]
            if esmovalue in fake_data:
                fake_data[fake_data.index(esmovalue)] = 'None+None'
                fake_data[row - 1] = esmovalue
            else:
                fake_data[row - 1] = esmovalue
            Bio(fake_data)

    Buttons((40, 30), 'Date', layer_2, ('Poppins', 16), '#cfb0b0', '#d57474', 5, '#FFA07A')
    Buttons((40, 70), 'Sex', layer_2, ('Poppins', 16), '#cfb0b0', '#d57474', 5, '#FFA07A')
    Buttons((40, 110), 'Xp', layer_2, ('Poppins', 16), '#cfb0b0', '#d57474', 5, '#FFA07A')
    Buttons((45, 250), 'Custom', layer_2, ('Poppins', 12), '#cfb0b0', '#d57474', 3, '#FFA07A')
    Buttons((150, 250), 'Delete', layer_2, ('Poppins', 12), '#cfb0b0', '#d57474', 3, '#FFA07A')
    Buttons((255, 225), 'Done', layer_2, ('Poppins', 12), '#7DC3F1', '#3286BD', 0, False)
    Buttons((255, 255), 'Back', layer_2, ('Poppins', 12), '#7DC3F1', '#3286BD', 0, False)
def edit_avatar():
    layer_2_wallpaper_C()
    global Profile_Image


    Button_change = blur_popup(('profile', 'ProfileEditor'), ((270,250), '#A13939'),'Build',
               button=((500,350),'Choose_File','Rounded',('#564E4E','#121212','#C2C57F',0),('Poppins' ,12),('Choose_File','edit_avatar'),(1,2)))
    round_rectangle(440, 190, 560, 310, '#E75151', 'None', canvas='blur_layer')
    Profile_Image = blur_popup(('profile', 'ProfileEditor'), ((550, 500), '#A13939'), 'Add',
                               image=((500, 250), data['profile_image'], 'profile_edit'))

    # def ask_file():
    #     ask_for_it = askopenfilename(title='Paradox-Assistant',
    #                                  filetypes=(('image files', '*.png'), ('image files', '*.jpg')))
    #     Ime = Image.open(ask_for_it)
    #     Image_blur = Ime.resize((300,300))
    #     Image_blur = ImageTk.PhotoImage(Image_blur.filter(ImageFilter.BoxBlur(10)))
    #     Ime = Ime.resize((100, 100))
    #     Image_try = ImageTk.PhotoImage(Ime)
    #     Lbl = Label(image =Image_try,width=100,height=100,bd=0)
    #     Lbl.image = Image_try
    #     LbL = Label(image =Image_blur,width=300,height=300,bd=0)
    #     layer_2.create_window((220,100),window=Lbl)
    #     layer_2.create_window((0,0),window=LbL,anchor='nw')
    #     LbL.image = Image_blur
    #
    # ask_file()
    # Text_With_A(('Save',('Poppins',14),'black','#7A2048'),layer_2,(220,120),'save_avatar',5,square='#CC313D')
def Profile_Editor():
    layer_2_wallpaper_C()
    round_rectangle(20, 20, 290, 250, '#F7C5CC', 'None')
    Text_With_A(('AVATAR', ('Indie Flower', 20), 'black', '#7A2048'), layer_2, (155, 70), 'edit_avatar', 5,
                square='#CC313D')
    Text_With_A(('Bio', ('Indie Flower', 22), 'black', '#7A2048'), layer_2, (155, 130), 'edit_bio', 4, square='#CC313D')
    Text_With_A(('Chng-Data', ('Indie Flower', 22), 'black', '#7A2048'), layer_2, (155, 193), 'edit_data', 4,
                square='#CC313D',sqale=(.6,1.1))
def search_profile(event = 'Update'):
    global _D_detry
    global d_tags
    global list_users
    layer_2_wallpaper_C()

    D_detry = []
    d_tags = []
    def Get_ALL_USERS(list_users):
        global user
        global page
        global show

        for i in d_tags:
            layer_2.delete(i)
        for i in D_detry:
            i.destroy()


        page = 0






        def show(page):
            for i in d_tags:
                layer_2.delete(i)
            for i in D_detry:
                i.destroy()
            row = 117
            r_config = 0
            for i in list_users[page * 4:]:
                data_configer = re.split('\|\*\*\|', i[3])
                User((75, row), (i[0] + '#' + data_configer[0], i[2], data_configer[1]))
                row += 30
                r_config += 1
                if r_config ==4:
                    break
            Text_With_A(('>', ('Poppins', 12, 'bold'), '#7824CA', '#8F50CD'), layer_2, (255, 235), 'p_fixer_T', 2)
            Text_With_A(('<', ('Poppins', 12, 'bold'), '#7824CA', '#8F50CD'), layer_2, (240, 235), 'p_fixer_F', 2)
            d_tags.append('>')
            d_tags.append('<')
        show(page)

    class User:
        def __init__(self, Cord, User_data):
            layer_2.create_line(Cord[0] - 4, Cord[1] - 3, Cord[0] - 4, Cord[1] + 23, width=3, fill='#8F37E5',tags = User_data[0])
            self.text = User_data[0]
            self.image_profile = BytesIO(bytes(User_data[1]))
            self.ima = ImageTk.PhotoImage(Image.open(self.image_profile).resize((20, 20)))
            self.image_profile.close()
            self.lbl = Label(image=self.ima, width=20, height=20, bd=1)
            self.lbl.image = self.ima
            layer_2.create_window((Cord[0] + 12, Cord[1] + 11), window=self.lbl)
            Text_With_A((self.text, ('Poppins', 10,'bold'), '#262626', '#7B9593'), layer_2, (Cord[0] + 26, Cord[1]),
                        'Search_profile', 0, moredata=('Search_profile', User_data), anchor='nw',bold='bold')
            d_tags.append(self.text)
            D_detry.append(self.lbl)

    if event == 'Update':
        user.execute('select * from Users')
        list_users = user.fetchall()

    round_rectangle(40, 30, 280, 250, '#CB8992', 'r_1')
    round_rectangle(60, 50, 220, 85, '#B5C4C4', 'r_1')
    v= StringVar(layer_2,value='Search....')
    entry = Entry(bd=0, width=14, font=('Poppins', 12), bg='#B5C4C4', textvariable=v, fg='black')
    entry.bind('<Button-1>',lambda event:entry.delete(0,END) if entry.get()=='Search....' else None)
    entry.bind('<KeyRelease>',lambda event:search_by_entry(entry.get()))
    layer_2.create_window((70,53),window=entry,anchor='nw')

    Get_ALL_USERS(list_users)
    def search_by_entry(text):
        global list_users
        data
        distance = []
        list_fixer = []
        for i in list_users:
            distance.append(((jellyfish.levenshtein_distance(i[0],text)),i))
        distance.sort(key = lambda x: x[0])
        list_users = []
        for i in distance:
            list_users.append(i[1])
        Get_ALL_USERS(list_users)
def Bio(DATA):
    global data_bio
    global l_c
    global APP_NAME

    tag_list = ['line-1', 'line-2', 'line-3', 'line-4']
    for i in tag_list:
        layer_1.delete(i)

    list_profile = []

    counter = 0
    layer_1.delete('line_bio')
    for i in DATA:
        popo = re.split('\+', i)
        Bold = False
        if popo[1] != 'None':
            y_pos_comfig = counter * 25 + 247
            if popo[0] in data.keys() or popo[1] in APP_NAME or popo[1] == 'Total-Xp':
                if popo[0] in data.keys():
                    layer_1.create_text((779, y_pos_comfig), text=popo[1] + ' -' + data[popo[0]],
                                        font=('Consolas', 12, 'bold'), anchor='sw', tags=tag_list[counter])
                else:
                    layer_1.create_text((779, y_pos_comfig), text=popo[1] + ' -' + popo[0],
                                        font=('Consolas', 12, 'bold'), anchor='sw', tags=tag_list[counter])
            else:
                layer_1.create_text((779, y_pos_comfig), text=popo[1], font=('Consolas', 12), anchor='sw',
                                    tags=tag_list[counter])
            layer_1.create_line(775, y_pos_comfig - 22, 775, y_pos_comfig + 3, width=4, tags='line_bio')
        counter += 1
    data_bio = DATA
    while len(data_bio) < 4:
        data_bio.append('None+None')
def layer_2_wallpaper_C():
    layer_2.delete('all')
    layer_2.create_image((0, 0), anchor='nw', image=image_layer2)
    layer_2.image = image_layer2
class App:
    def __init__(self, APP_DATA, Cordinate, size, font):
        # app_data = 1- image_dir 2- cmd 3- app description
        global layer_1
        global images
        self.image_name = APP_DATA[0]
        self.img_open = Image.open(images[APP_DATA[0]])
        self.img_animate = ImageTk.PhotoImage(self.img_open.resize((105, 105), Image.ANTIALIAS))
        self.image = ImageTk.PhotoImage(self.img_open)
        self.tip = APP_DATA[2]
        self.size = size
        self.img = layer_1.create_image(Cordinate, image=self.image, tag=self.tip)
        layer_1.ima = self.image
        layer_1.tag_bind(self.tip, '<Enter>', lambda event: self.animate(True))
        layer_1.tag_bind(self.tip, '<Leave>', lambda event: self.animate(False))
        layer_1.tag_bind(self.tip, '<Button-1>', lambda event: self.command_runner(APP_DATA[1]))
        self.text = layer_1.create_text((Cordinate[0], Cordinate[1] + self.size / 1.35), text=self.tip, font=font)

    def animate(self, event):
        if event:
            layer_1.itemconfigure(self.tip, image=self.img_animate)
        else:
            layer_1.itemconfigure(self.tip, image=self.image)

    def command_runner(self, command):
        if command == 'Bio_Editer':
            Profile_Editor()
        if command == 'Search_profile':
            search_profile()
        if command == 'lesson_chem_jadval':
            l_jadval_Tanavobi()

    def destroy(self):
        layer_1.delete(self.img)
        layer_1.delete(self.text)
def L_layer_clear():
    global layer_2
    layer_2.delete('all')
    img_layer_2 = ImageTk.PhotoImage(Image.open(images['profile_layer_2']))
    layer_2.create_image((0, 0), image=img_layer_2, anchor='nw')
    layer_2.image = img_layer_2
def l_jadval_Tanavobi():
    global layer_2
    L_layer_clear()
    Text_With_A(('Start',('Poppins',16),'#1e2b8f','#0c155c'),layer_2,(372,204),
                'Chem_Jadval_Test',5,square='#babdd7',sqale=(4,2))


def game():
    global main_surface
    global layer_1
    global images
    global Current_apps
    global app_list
    global count

    count = 0
    Current_apps = []
    app_list = [('test', None, 'Unknown'), ('test2', None, 'Unknown'), ('test3', None, 'Unknown'),
                ('test4', None, 'Unknown'), ('test5', None, 'Unknown')]

    def update_apps(event):
        global count
        global Current_apps
        global app_list

        if event:
            count += 1
            for capp in Current_apps:
                capp.destroy()
            Current_apps = []

            x_pos = 730
            counter = 0
            if len(app_list[count:]) == 2:
                count -= 1
            for now in app_list[count:]:
                Current_apps.append(App(now, (x_pos, 150), 90, ('Poppins 14')))
                x_pos += 105
                if counter == 2: break
                counter += 1
        else:
            count -= 1
            for capp in Current_apps:
                capp.destroy()
            Current_apps = []

            x_pos = 730
            counter = 0
            if count == -1: count += 1
            for now in app_list[count:]:
                Current_apps.append(App(now, (x_pos, 150), 90, ('Poppins 14')))
                x_pos += 105
                if counter == 2: break
                counter += 1

    main_surface.title('Game')
    layer_1.delete('all')
    wallpaper_game = ImageTk.PhotoImage(Image.open(images['game_wallpaper']))
    layer_1.create_image((0, 0), image=wallpaper_game, anchor='nw')
    layer_1.image = wallpaper_game

    l2_image = ImageTk.PhotoImage(Image.open(images['game_l2']))
    layer_2 = Canvas(width=460, height=400, bg='black', bd=0, relief='sunken', highlightthickness=0)
    layer_2.create_image((0, 0), anchor='nw', image=l2_image)
    layer_2.image = l2_image
    layer_1.create_window((92, 45), anchor='nw', window=layer_2)

    exit_img = ImageTk.PhotoImage(Image.open(images['game_exit']))
    button_exit = Button(bd=0, image=exit_img, justify='left', relief='sunken', width=17, height=20, command=menu)
    button_exit.image = exit_img
    layer_1.create_window((75, 20), anchor='nw', window=button_exit)

    next_img = ImageTk.PhotoImage(Image.open(images['game_next']))
    button_next = Button(bd=0, image=next_img, justify='left', relief='sunken', width=38, height=40,
                         command=lambda: update_apps(True))
    button_next.image = next_img
    layer_1.create_window((607, 66), anchor='nw', window=button_next)

    prevoius_img = ImageTk.PhotoImage(Image.open(images['game_previous']))
    button_prevoius = Button(bd=0, image=prevoius_img, justify='left', relief='sunken', width=40, height=30,
                             command=lambda: update_apps(False))
    button_prevoius.image = prevoius_img
    layer_1.create_window((609, 180), anchor='nw', window=button_prevoius)

    con = 0
    x_pos = 730

    for i in app_list:
        Current_apps.append(App(i, (x_pos, 150), 90, ('Poppins 14')))
        x_pos += 105
        if con == 2:
            break
        con += 1
def learn():
    global main_surface
    global layer_1
    global images
    global page
    global d_list
    global layer_2


    main_surface.title('Learn')
    layer_1.delete('all')

    layer_2=Canvas(layer_1,width=744,height=408,bd=0, relief='sunken', highlightthickness=0)
    layer_1.create_window((45,38),anchor='nw',window=layer_2)
    img_layer_2 = ImageTk.PhotoImage(Image.open(images['profile_layer_2']))
    layer_2.create_image((0,0),image=img_layer_2,anchor='nw')
    layer_2.image = img_layer_2
    wallpaper_learn = ImageTk.PhotoImage(Image.open(images['learn_wallpaper']))
    layer_1.create_image((0, 0), image=wallpaper_learn, anchor='nw')
    layer_1.image = wallpaper_learn

    back_but = layer_1.create_text((980,20),text='Back',anchor ='ne',font=('Poppins',16),tags='back',fill = '#8FA2BD')
    layer_1.tag_bind('back','<Button-1>',lambda event:menu())
    layer_1.tag_bind('back','<Enter>',lambda event:layer_1.itemconfigure(back_but,fill='#6972B3',font=('Poppins',18)))
    layer_1.tag_bind('back', '<Leave>', lambda event: layer_1.itemconfigure(back_but, fill='#8FA2BD',font=('Poppins',16)))

    app_related = []
    lesson_app_ids = ['0010','0020']
    for i in APPS:
        for y in lesson_app_ids:
            if i['id']==y:
                app_related.append(i)
    page = 0
    def page_C(event):
        global page
        if event == 'Next' and  page+1 <= len(app_related)-1:
            page+=1
            show(page)
        if event == 'P' and page-1 != -1:
            page-=1
            show(page)
    d_list = []
    def show(page):
        global d_list
        if len(d_list) != 0:
            d_list[0].destroy()
            layer_1.delete(d_list[1])
            layer_1.delete(d_list[2])
            d_list=[]
        C_pos = 100
        i= app_related[page]
        Obj = App((i['icon_dir'],i['command'],i['description']),(C_pos,521),90,('Poppins',12))
        next_B = layer_1.create_text((20,510),text = '>',font=('Poppins 20'),tags = 'next',fill='#3E415A')
        next_P = layer_1.create_text((20, 570), text='<', font=('Poppins 20'), tags='pervious',fill='#3E415A')
        layer_1.tag_bind('next','<Button-1>',lambda event:page_C('Next'))
        layer_1.tag_bind('pervious', '<Button-1>', lambda event: page_C('P'))
        layer_1.tag_bind('next','<Enter>',lambda event:layer_1.itemconfigure('next',fill='#222865'))
        layer_1.tag_bind('next', '<Leave>', lambda event: layer_1.itemconfigure('next', fill='#3E415A'))
        layer_1.tag_bind('pervious', '<Enter>', lambda event: layer_1.itemconfigure('pervious', fill='#222865'))
        layer_1.tag_bind('pervious', '<Leave>', lambda event: layer_1.itemconfigure('pervious', fill='#3E415A'))
        d_list.append(Obj)
        d_list.append('next')
        d_list.append('pervious')
    show(page)
def menu():
    global images
    global layer_1
    global main_surface

    main_surface.title('Menu')
    layer_1.delete('all')
    image_main = ImageTk.PhotoImage(Image.open(images['main']))
    image_learn = ImageTk.PhotoImage(Image.open(images['learn']))
    image_game = ImageTk.PhotoImage(Image.open(images['game']))
    image_profile = ImageTk.PhotoImage(Image.open(images['profile']))

    layer_1.create_image((0, 0), image=image_main, anchor='nw')
    layer_1.image = image_main

    learn_But = Button(layer_1, image=image_learn, bd=0, justify='left', relief='sunken', width=338, height=188,
                       command=learn)
    learn_But.image = image_learn
    layer_1.create_window((1000, 0), anchor='ne', window=learn_But)

    game_but = Button(layer_1, image=image_game, bd=0, justify='left', relief='sunken', width=257, height=181,
                      command=game)
    game_but.image = image_game
    layer_1.create_window((0, 0), anchor='nw', window=game_but)

    profile_but = Button(layer_1, image=image_profile, bd=0, relief='sunken', width=352, height=180, command=profile)
    profile_but.image = image_profile
    layer_1.create_window((0, 600), anchor='sw', window=profile_but)


def profile():
    global main_surface
    global layer_1
    global layer_2
    global APPS
    global image_layer2
    global data

    image_layer2 = ImageTk.PhotoImage(Image.open(images['profile_frame']))

    app_profile = ['0001', '0002']
    app_contain = []
    for i in APPS:
        for y in app_profile:
            if i['id'] == y:
                app_contain.append(i)

    main_surface.title('Profile')
    layer_1.delete('all')
    Image_wallpaper = ImageTk.PhotoImage(Image.open(images['profile_wallpaper']))
    layer_1.create_image((0, 0), image=Image_wallpaper, anchor='nw')
    layer_1.image = Image_wallpaper

    layer_2 = Canvas(width=315, height=270, bd=0, relief='sunken', highlightthickness=0)
    layer_1.create_window((64, 62), anchor='nw', window=layer_2)
    layer_2_wallpaper_C()

    back_image = ImageTk.PhotoImage(Image.open(images['profile_exit']))
    back_button = Button(image=back_image, width=80, height=55, relief='sunken', bd=0, command=menu)
    back_button.image = back_image
    layer_1.create_window((4, 600), anchor='sw', window=back_button)
    layer_1.create_text((877, 195), text=data['username'], font=('Poppins 18 bold'))

    stream = BytesIO(data['profile_image'])
    prof_image = Image.open(stream).convert('RGBA')
    stream.close()
    prof_image = ImageTk.PhotoImage(prof_image)
    profile_img = Label(image=prof_image)
    profile_img.image = prof_image
    img = layer_1.create_window((877, 120), window=profile_img)
    layer_1.create_text((877, 120), text=data['username'], font=('Poppins 18 bold'))
    Bio(data['bio'])

    global page
    global c_app
    page = 0
    c_app = []

    def show_app(event):
        global page
        global c_app
        if c_app != []: c_app.destroy()
        if event == True and page + 1 < len(app_contain):
            page += 1
        elif event == False and page - 1 != -1:
            page -= 1
        app = app_contain[page]
        c_app = App((app['icon_dir'], app['command'], app['description']), (270, 520), 90, ('Poppins 14'))

    def animate(tag, event):
        if event:
            layer_1.itemconfigure(tag, font=('Poppins 24 bold'), fill='dark red')
        else:
            layer_1.itemconfigure(tag, font=('Poppins 20 bold'), fill='black')

    b_next = layer_1.create_text((326, 590), text='>', font=('Poppins 20 bold'), tag='NU')
    b_undo = layer_1.create_text((215, 590), text='<', font=('Poppins 20 bold'), tag='UN')
    layer_1.tag_bind('NU', '<Enter>', lambda event: animate('NU', True))
    layer_1.tag_bind('NU', '<Leave>', lambda event: animate('NU', False))
    layer_1.tag_bind('UN', '<Enter>', lambda event: animate('UN', True))
    layer_1.tag_bind('UN', '<Leave>', lambda event: animate('UN', False))
    layer_1.tag_bind('NU', '<Button-1>', lambda event: show_app(True))
    layer_1.tag_bind('UN', '<Button-1>', lambda event: show_app(False))
    show_app(None)


def send_get_data():
    global conector
    global username

    nc = conector.cursor()
    t_xp = 0
    for i in APPS:
        if i['xp'] != None:
            t_xp += int(i['xp'])
    bio = ''
    for i in data['bio']:
        if data['bio'].index(i) == 3:bio = bio+i.strip()
        else:bio = bio+i.strip() + '=--=--='
    datatosend = (data['username'], data['password'], bytes(data['profile_image']),
                  data['id'] + '|**|' + bio + '|**|' + data['sex'] + '|**|' + data['xp'] + '|**|' + data[
                      'date_create'] + '|**|', username)
    cmd = "UPDATE Users SET username = %s,password=%s,profile=%s,moredata=%s WHERE username=%s"
    nc.execute(cmd, datatosend)
    conector.commit()


menu()
main_surface.mainloop()
