import requests
import random
from tkinter import *
from PIL import Image,ImageTk
import re

def get_a_person():
    r = requests.get('https://randomuser.me/api/')
    data = r.json()['results'][0]
    picture_byte = requests.get(data['picture']['large']).content
    with open('saved_pic.png','wb') as w:
        w.write(picture_byte)

    t_data = {
        'name' : data['name']['first']+' '+data['name']['last'],
        'email' : data['email'],
        'username' : data['login']['username'],
        'password' : data['login']['password'],
        'date_of_birth' : data['dob']['date'],
        'age' : data['dob']['age'],
        'phone' : data['cell'],
        'gender' : data['gender'],
        'location_details' : {
            'country' : data['location']['country'],
            'city' : data['location']['city'],
            'state' : data['location']['state'],
            'street' : data['location']['street']['name'],
            'postcode' : data['location']['postcode'],
        }
    }
    print(data['dob']['date'])
    return t_data






datas = get_a_person()

root = Tk()
root.title('Pesky Bird')
orig_pic = ImageTk.PhotoImage(Image.open('saved_pic.png'))
canvas = Canvas(root,width = 400,height = 300,bg='#196D76')
canvas.pack(anchor='nw')
canvas.create_rectangle(25,25,375,275,fill='#7DCED6')
obj=canvas.create_image(40,40,image = orig_pic,anchor='nw')
canvas.create_rectangle(37,37,42+orig_pic.width(),42+orig_pic.height())
canvas.create_text(180,85,text='Name:  ' + datas['name'],anchor='nw')
canvas.create_text(180,105,text='Gender:  ' + datas['gender'],anchor='nw')
canvas.create_text(180,125,text='Age:  ' + str(datas['age']),anchor='nw')
canvas.create_text(240,125,text='D-Of-Birth:  ' + str(datas['date_of_birth']),anchor='nw')
root.mainloop()