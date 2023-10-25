# forms.py

from django import forms
from .models import Car
from .models import Order

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['carName', 'carType', 'carDescription', 'carRate']
        fields = ['carName', 'carType', 'carDescription', 'carRate', 'carPic']

