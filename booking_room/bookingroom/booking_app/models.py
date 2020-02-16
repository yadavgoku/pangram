from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Booking(models.Model):
    ROOM_CHOICES = (("ganga","ganga"),
                    ("yamuna","yamuna"),
                    ("sarswathi","sarswathi"))

    name = models.ForeignKey(User,on_delete=models.CASCADE)
    room = models.CharField(max_length=10,choices=ROOM_CHOICES,default=1)
    date = models.DateField(default=timezone.now)



