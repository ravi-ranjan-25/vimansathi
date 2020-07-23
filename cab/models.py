from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class carClass(models.Model):
    cartype = models.CharField(max_length=50,unique=True)
    seat = models.IntegerField(default=1,max_length=1)
    

class cabdetails(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    cartype = models.ForeignKey(carClass,on_delete = models.CASCADE)
    carModel = models.CharField(max_length=50,unique=False)
    carRegistration = models.CharField(max_length=50,unique=True)
    carColor = models.CharField(max_length=10,unique=False)
    rating = models.FloatField(default=1,max_length=4)
    totalRides = models.IntegerField(default=0,max_length=10)
    rating = models.FloatField(default=1,max_length=10)
    

    def __str__(self):
        return self.user.username    

class cabOrder(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    cab = models.ForeignKey(cabdetails,on_delete = models.CASCADE,null=True)
    cartype = models.ForeignKey(carClass,on_delete = models.CASCADE,null=True,default=None)
    origin = models.CharField(unique=False,max_length=256)
    cabid = models.CharField(unique=True,max_length=256)
    destination = models.CharField(unique=False,max_length=256)
    latitudeOrigin = models.CharField(unique=False,max_length=256)
    longitudeOrigin = models.CharField(unique=False,max_length=256)
    latitudeDestination = models.CharField(unique=False,max_length=256)
    longitudeDestination = models.CharField(unique=False,max_length=256)
    seat = models.IntegerField(default=1,max_length=256)
    price=models.FloatField(default=0,max_length=256)
    accept = models.IntegerField(default=-1,max_length=256)
    time = models.DateTimeField(default = timezone.now())
    pickupTime = models.DateTimeField(default = timezone.now())
    rating = models.FloatField(default=0,max_length=10)


    def __str__(self):
        return self.cabid