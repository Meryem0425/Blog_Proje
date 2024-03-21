
import datetime
from django.db import models


class arama(models.Model):
    name= models.CharField(max_length=255)
    description = models.TextField(max_length=1000,blank=True)  
    image = models.ImageField(upload_to='static/images/' , blank=True, null=True)
    date = models.DateField() 
    


def __str__(self):
    return self.name




