from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=10)
    desc=models.TextField()
    
    def __str__(self):
        return self.name

class Blog(models.Model):
    title=models.CharField(max_length=80)
    authname=models.CharField(max_length=30)
    bdesc=models.TextField()
    img=models.ImageField(upload_to='photo',blank=True,null=True)
    date=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self) :
        return self.title
    
    