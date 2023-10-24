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

class Order(models.Model):
    order_number = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    car_name = models.CharField(max_length=255)
    date_range = models.DateField(max_length=100)  # You might want to use a DateField for actual dates
    total = models.DecimalField(max_digits=10, decimal_places=2)
