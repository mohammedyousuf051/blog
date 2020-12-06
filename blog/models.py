from django.db import models
from rest_framework.authentication import get_user_model
from datetime import date
from django.utils import timezone



class blogs(models.Model):
    # id = models.IntegerField(primary_key=True)
    name=models.CharField(max_length=255,unique=True)
    description=models.CharField(max_length=255,default="",null=True,blank=True)
    detail=models.TextField(default="",null=True,blank=True)
    image=models.TextField(default="",null=True,blank=True)
    created_date=models.DateTimeField(default=timezone.now)
    creator = models.CharField(max_length=255,default="",null=True,blank=True)
    users=models.ManyToManyField(get_user_model())

    def __str__(self):
        return str(self.name)


class blogcomments(models.Model):
    # id = models.IntegerField(primary_key=True)
    name=models.ForeignKey(blogs, on_delete=models.CASCADE)
    comment=models.TextField(default="",null=True,blank=True)
    created_date=models.DateTimeField(default=timezone.now)
    creator = models.CharField(max_length=255,default="",null=True,blank=True)
    users=models.ManyToManyField(get_user_model())

    def __str__(self):
        return str(self.name) + "_" + str(self.id)
