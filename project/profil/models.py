from django.db import models


# Create your models here.


class Profil(models.Model):
    name=models.CharField(max_length=20)
    position=models.CharField(max_length=40)
    selfdesc=models.TextField()
    age=models.IntegerField()
    phone=models.CharField(max_length=10)
    city=models.CharField(max_length=40)
    edu=models.CharField(max_length=40)
    email=models.EmailField()
    gender=models.CharField(max_length=40)

class img(models.Model):
    img=models.ImageField(upload_to='photo',blank=True,null=True)
    bgimg=models.ImageField(upload_to='photo',blank=True,null=True)


