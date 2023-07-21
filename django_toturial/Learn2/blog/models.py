from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Posts(models.Model):
    Title = models.CharField(max_length=100)
    Content = models.CharField(max_length=500)
    date_posted = models.TimeField(default=timezone.now)
    Author = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Title