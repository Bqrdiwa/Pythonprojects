from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import User, ItemLike

@receiver(post_save, sender = User)
def create_item_like(sender, instance, created,**kwargs):
    if created:
        ItemLike.objects.create( userRelated =instance)