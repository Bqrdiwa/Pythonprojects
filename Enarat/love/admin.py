from django.contrib import admin
from .models import Gallery, Item, ItemLike, User, ItemMSG, Post, Log, Another
# Register your models here.

admin.site.register(Gallery)
admin.site.register(Item)
admin.site.register(ItemLike)
admin.site.register(User)
admin.site.register(ItemMSG)
admin.site.register(Post)
admin.site.register(Log)
admin.site.register(Another)