from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
priviledges = (
    ('admin','ADMIN'),
    ('user','USER'),
)

class UserProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    email = models.CharField(max_length=255,default="",blank=True,null=True)
    priviledge = models.CharField(max_length=6, choices=priviledges, default='user')
    profile_pic = models.TextField(default="",blank=True,null=True)

    def __str__(self):
        return self.user.username