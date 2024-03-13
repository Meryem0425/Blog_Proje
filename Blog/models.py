from django.db import models


class arama(models.Models):
    name= models.CharField(max_lenght=255)
    def __str__(self):
        return self.name
    
# Create your models here.
