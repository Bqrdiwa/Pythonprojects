from channels.generic.websocket import AsyncWebsocketConsumer
from channels.exceptions import StopConsumer
import json
from .models import ItemMSG, Gallery, Item
from channels.db import database_sync_to_async
import jdatetime
import base64
import locale
from django.core.files.base import ContentFile
from .models import Post
import pytz
from .models import User
from django.db.models import Q

class LoveConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['albumName'].replace(' ', '')
        self.gallery_name = self.scope['url_route']['kwargs']['albumName']
        self.user = self.scope['user']
        print('username '+  self.user.username)
        await self.database_handeler('initiate')
        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )
        await self.accept()
    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name
)
        raise StopConsumer()
    async def receive(self, text_data):
        DICT_DATA = json.loads(text_data)
        action = DICT_DATA['action']
        if action == 'GET_MSG':
            msgs = await self.database_handeler(action=action, data ={'pk':DICT_DATA['item']})
            await self.send(json.dumps({
                'action': 'pong-msgs',
                'msgs': msgs
            }))
        elif action == 'GET_ITEMS':
            items = await self.database_handeler(action = action)
            await self.send(json.dumps({
                'action': 'pong-items',
                'items': items
            }))
        elif action == 'SEND_MSG':
            msg = await self.database_handeler(action= action, data = {'msg':DICT_DATA['msg'], 'itemPK': DICT_DATA['itemPK']})
            await self.channel_layer.group_send(
                self.room_name,
                {
                    'type':'group_handeler',
                    'action':'appendMSG',
                    'msg':msg
                }
            )
        elif action =='delete':
            await self.database_handeler(action = 'delete', data ={'item': DICT_DATA['item']})
            await self.channel_layer.group_send(
                self.room_name,
                {
                    'type':'group_handeler',
                    'action':'delete',
                    'item':DICT_DATA['item']
                }
            )
        elif action =='ADDIMG':
            imgDetails =  await self.database_handeler('ADDIMG', data= {'image':DICT_DATA['image']})
            await self.channel_layer.group_send(
                self.room_name,
                {
                    'type':'group_handeler',
                    'action':'add-post',
                    'detail':imgDetails
                }
            )
        elif action == 'post':
            await self.database_handeler(action ='post', data ={'item':DICT_DATA['item'], 'desc':DICT_DATA['desc']})
        elif action =='add-user':
            username = DICT_DATA['username']
            yOfAdding = await self.database_handeler(action= action, data ={'username':username})
            print(yOfAdding)
            if yOfAdding:
                await self.channel_layer.group_send(
                    self.room_name,
                    {
                        'type':'group_handeler',
                        'action':'add-user',
                        'username': username,
                    }
                )
            else:
                await self.send(json.dumps({
                    'action':'add-user',
                    'username':'None',
                    'response':'False'
                }))
        elif action == 'GET_USERS':
            users = await self.database_handeler(action=action)
            await self.send(json.dumps({
                'action':'pong-users',
                'users':users
            }))
        elif action == 'delete-user':
            username = DICT_DATA['username']
            await self.database_handeler(action = action, data ={'username': username})
            await self.channel_layer.group_send(
                self.room_name,
                {
                    'type':'group_handeler',
                    'action':'delete-user',
                    'username': username
                }
            )
    async def group_handeler(self,data):
        action = data['action']
        if action == 'appendMSG':

            await self.send(json.dumps({
                'action': 'appendMSG',
                'msg':data['msg']
            }))
        elif action == 'delete':
            await self.send(json.dumps({
                'action': 'delete',
                'item':data['item']
            }))
        elif action == 'add-post':
            await self.send(json.dumps({
                'action':action,
                'detail':data['detail']
            }))
        elif action =='add-user':
            await self.send(json.dumps({
                'action':'add-user',
                'username':data['username'],
                'response':'True'
            }))
        elif action == 'delete-user':
            await self.send(json.dumps({
                'action':'delete-user',
                'username':data['username']
            }))
    def MSGToDict(self, msg):
        local_timezone = pytz.timezone('Asia/Tehran')
        msg_date = msg.date_created
        msg_date = msg_date.astimezone(local_timezone)
        msg_day = int(msg_date.strftime('%d'))
        msg_month = int(msg_date.strftime('%m'))
        msg_year = int(msg_date.strftime('%Y'))

        year, month, day = jdatetime.GregorianToJalali(msg_year,  msg_month ,msg_day).getJalaliList()
        persian_date_time = jdatetime.datetime(year,month, day)
        
        msg_time = f'{msg_date.hour}:{msg_date.minute}'
        compiled_time = persian_date_time.strftime('%B.%d %A')
                
        return {
                    'sender':msg.userRelated.username,
                    'content':msg.message,
                    'time':msg_time,
                    'date':compiled_time,
                    'album':msg.itemRelated.pk,
                    'pk':msg.pk
                }
    @database_sync_to_async
    def database_handeler(self, action, data=None):
        if action == 'initiate':
            self.gallery = Gallery.objects.get(title= self.gallery_name)
        elif action == 'GET_MSG':
            item_to_get_msg_from = Item.objects.get(pk= data['pk'])
            raw_msgs = ItemMSG.objects.all().filter(itemRelated = item_to_get_msg_from)
            cooked_msgs = []
            locale.setlocale(locale.LC_TIME, 'en_US.utf8')
            for msg in raw_msgs:
                cooked_msgs.append(self.MSGToDict(msg))
            return cooked_msgs
        elif action == 'GET_ITEMS':
            items = self.gallery.get_all_items
            images = []
            local_timezone = pytz.timezone('Asia/Tehran')
            for image in items:
                dc = image.date_created
                dc = dc.astimezone(local_timezone)
                persian_datetime = jdatetime.datetime.fromgregorian(datetime= dc)
                ymd= persian_datetime.strftime('%Y/%m/%d - %H:%M')
                dateCreated = f'{ymd}'

                images.append({
                    'file':image.file.url,
                    'creator':image.creator.username,
                    'pk':image.pk,
                    'date_created':dateCreated
                })
            return images
        elif action == 'SEND_MSG':
            itemR = Item.objects.get(pk=data['itemPK'])
            msg = ItemMSG.objects.create(
                userRelated= self.user,
                galleryRelated= self.gallery,
                message = data['msg'],
                itemRelated = itemR
                )
            dict_data =self.MSGToDict(msg)
            return dict_data
        elif action == 'delete':
            ITEM_TO_REMOVE = Item.objects.get(pk = data['item'])
            ITEM_TO_REMOVE.delete()
            print('item deleted')
        elif action =='post':
            ITEM_TO_POST = Item.objects.get(pk = data['item'])
            NEW_POST = Post.objects.create(desc = data['desc'], item = ITEM_TO_POST)
        elif action == 'ADDIMG':
            _,encoded = data['image'].split(',',1)
            bd = base64.b64decode(encoded.encode('utf-8'))
            image = Item.objects.create(creator = self.user, AlbumRelated = self.gallery)
            image.file.save(f'{image.pk}.png',  ContentFile(bd))
            dc = image.date_created
            local_timezone = pytz.timezone('Asia/Tehran')
            dc = dc.astimezone(local_timezone)
            persian_datetime = jdatetime.datetime.fromgregorian(datetime= dc)
            ymd= persian_datetime.strftime('%Y/%m/%d - %H:%M')
            dateCreated = f'{ymd}'
            print('new im added')
            return {
                'file':image.file.url,
                'creator':image.creator.username,
                'pk':image.pk,
                'date_created':dateCreated
            }

        elif action == 'add-user':
            username = data['username']
            if username != self.user.username:   
                try:
                    user = User.objects.get(username = username)  
                    if not user.groups.filter(name='admin').count() > 0:
                        self.gallery.users.add(user)
                        return True
                    else:
                        return False
                except:
                    return False
        elif action == 'delete-user':
            user= User.objects.get(username = data['username'])
            if user in self.gallery.users.all():
                self.gallery.users.remove(user)
        elif action == 'GET_USERS':
            cooked_users = []
            admin_users = User.objects.filter(
                groups__name='admin')
            album_users = self.gallery.users.all()
            users = admin_users | album_users
            users.distinct()
            
            for user in users:
                cooked_users.append(user.username)
            return cooked_users
        