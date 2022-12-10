from django.db import models

# Create your models here.
class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.TextField(default=False)

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    email = models.EmailField()
    phnno= models.TextField()
    loanamount = models.BigIntegerField()
    university = models.TextField()
    course = models.TextField()
    workexp = models.TextField()