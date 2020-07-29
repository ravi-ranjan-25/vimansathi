from django.db import models
from django.utils import timezone

# Create your models here.
class userinteraction(models.Model):
    USER_ID= models.CharField(max_length=50,unique=False)
    ITEM_ID = models.CharField(max_length=50,unique=False)
    EVENT_TYPE = models.CharField(max_length=50,unique=False)
    EVENT_VALUE = models.CharField(max_length=50,unique=False)
    TIMESTAMP = models.DateTimeField(default = timezone.now())

    def __str__(self):
        return self.USER_ID    
