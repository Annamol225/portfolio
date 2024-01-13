from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=10)
    desc=models.TextField()
    
    def __str__(self):
        return self.name