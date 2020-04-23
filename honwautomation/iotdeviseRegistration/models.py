from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Registerdevice(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.PROTECT)
    deviceID = models.CharField(max_length=16,unique=True)
    registerdatatime = models.DateTimeField(auto_now=True)
    logo = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.deviceID
