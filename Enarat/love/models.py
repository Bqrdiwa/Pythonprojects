from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,  UserManager, Group, Permission, AbstractUser
from .manager import CustomUserManager
from django.utils.translation import gettext as _
from django.utils import timezone
from django.contrib.auth.models import Permission
from jdatetime import datetime
import pytz

# Create your models here.
class User(PermissionsMixin, AbstractBaseUser):
    username = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=256)
    date_created  = models.TimeField(default=timezone.now)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'

    

    groups = models.ManyToManyField(
        Group,
        verbose_name=_("groups"),
        blank=True,
        help_text=_(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        related_name="love_user_set",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_("user permissions"),
        blank=True,
        help_text=_("Specific permissions for this user."),
        related_name="love_user_set",
    )
    objects = CustomUserManager()
    def __str__(self):
        return self.username
    
class Gallery(models.Model):
    title = models.CharField(max_length=12)
    date_created = models.TimeField(default=timezone.now)
    thumbnail = models.ImageField(upload_to='albums-thumbnails', default='/albums-thumbnails/default.png')
    users = models.ManyToManyField(User)
    
    @property
    def get_all_items(self):
        return Item.objects.all().filter(AlbumRelated = self)
    def __str__(self):
        return self.title

class Item(models.Model):
    AlbumRelated = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    file = models.FileField(upload_to='Albums-items/')
    
    @property
    def likes(self):
        return self.itemlike_set.all().count()
        
        
    def __str__(self):
        return self.AlbumRelated.title+"'s" +' Image'

class ItemLike(models.Model):
    itemRelated = models.ManyToManyField(Item)
    userRelated = models.OneToOneField(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.userRelated.username +"'s Panel"
    
class ItemMSG(models.Model):
    itemRelated = models.ForeignKey(Item, on_delete= models.CASCADE)
    galleryRelated = models.ForeignKey(Gallery,null=True, on_delete=models.CASCADE)
    message = models.CharField(max_length=64)
    userRelated = models.ForeignKey(User, on_delete= models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    
class Post(models.Model):
    desc = models.CharField(max_length=48)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    where = models.CharField(max_length=24, default='CAN_FIND')
    time = models.DateTimeField(default=timezone.now)
    def __str__(self):
        local_timezone = pytz.timezone('Asia/Tehran')
        time = self.time.astimezone(local_timezone)
        time = datetime.fromgregorian(datetime =time)
        time = time.strftime('%Y/%m/%d - %H:%M')
        
        return f'{self.user.username} visited {self.where} in {time}'
class Another(models.Model):
    anotherOp = models.CharField(max_length=480)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    time_sended = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f'{self.anotherOp} By {self.sender.username}'