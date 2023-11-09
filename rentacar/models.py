from django.db import models
from django.contrib.auth.models import User
from django.db.models import F
import random
import string

class Car(models.Model):
    CarID = models.AutoField(primary_key=True)
    carName = models.CharField(max_length=255)
    carType = models.CharField(max_length=100)
    carDescription = models.TextField()
    carRate = models.FloatField()
    carPic = models.ImageField(upload_to='car_pics/', blank=True, null=True)
    status = models.IntegerField(default=0)
    
    availability = models.IntegerField(default=0)

    def __str__(self):
        return self.carName

class Order(models.Model):
    PENDING = 0
    CONFIRMED = 1
    CANCELED = 2

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (CONFIRMED, 'Confirmed'),
        (CANCELED, 'Canceled'),
    ]

    orderNumber = models.CharField(max_length=8, primary_key=True, unique=True)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    carid = models.ForeignKey(Car, on_delete=models.CASCADE)
    carName = models.CharField(max_length=255)
    startDate = models.DateField(default=None)
    endDate = models.DateField(default=None)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.FloatField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=PENDING)  # New status field

    def __str__(self):
        return self.orderNumber