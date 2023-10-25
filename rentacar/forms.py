# forms.py

from django import forms
from .models import Car
from .models import Order

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['carName', 'carType', 'carDescription', 'carRate']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['carid', 'startDate', 'endDate', 'duration']  # Fields you want to include in the form