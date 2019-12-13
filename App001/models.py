from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=12)
    data = models.DateTimeField(auto_now_add=True)

class IDCard(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    nation = models.CharField(max_length=10)
    sex = models.CharField(max_length=1)
    idnum = models.CharField(max_length=18)
    address = models.CharField(max_length=50)
    session = models.CharField(max_length=10)
    data = models.DateTimeField(auto_now_add=True)
