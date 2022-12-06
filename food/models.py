from django.db import models
import datetime
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,)
    fname = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    stock = models.IntegerField()
    price = models.IntegerField()
    fatcat = models.CharField(max_length=255)
    yngvi = models.CharField(max_length=255)

class Resto(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,)
    rname = models.CharField(max_length=255)
    rbranch = models.CharField(max_length=255)
    rating = models.IntegerField()
    rphone = models.IntegerField()
    rstreet = models.CharField(max_length=255)
    rdistrict = models.CharField(max_length=255)
    rcity = models.CharField(max_length=255)
    rprovince = models.CharField(max_length=255)
    rcat = models.CharField(max_length=255)
    opday = models.CharField(max_length=255)
    opstart = models.TimeField
    opend = models.TimeField
