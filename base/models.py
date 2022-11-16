from django.db import models

class User(models.Model):
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=50)
    birthdate = models.DateField()
        
