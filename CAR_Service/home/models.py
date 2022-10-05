import sqlite3
from django.db import models

# Create your models here.

class home(models.Model):
    fullname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phonenumber = models.IntegerField(max_length=50)
    confirmpassword= models.CharField(max_length=50)
    gender= models.CharField(max_length=50)

class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    