from django.db import models
from django.contrib.auth.models import User
from django.db.models import F

class Car(models.Model):
    CarID = models.AutoField(primary_key=True)
    carName = models.CharField(max_length=255)
    carType = models.CharField(max_length=100)
    carDescription = models.TextField()
    carRate = models.DecimalField(max_digits=10, decimal_places=2)
    carPic = models.ImageField(upload_to='car_pics/', blank=True, null=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.carName
