from django.db import models

# Create your models here.

class Usuarios(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=32)
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    role = models.SmallIntegerField()
    date_added = models.DateTimeField(auto_now=True) 
    
	