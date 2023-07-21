from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import User, Profile

@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(userRelated = instance)
        
@receiver(post_save, sender = Profile)
def update_profile(sender, instance, **kwargs):
    default_profile = instance.image
    default_profiles = ['default.png', 'girl.png', 'boy.png']
    sex = instance.sex
    default = False
    access = True
    if sex+'.png' == default_profile:
        access = False
    if default_profile in default_profiles:
        default = True
        
    if instance.sex == 'boy' and default and access:
        instance.image = 'boy.png'
        instance.save()
    elif instance.sex == 'girl' and default and access:
        instance.image = 'girl.png'
        instance.save()
        
        
