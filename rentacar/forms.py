# forms.py

from django import forms
from .models import Car
<<<<<<< HEAD
=======
from .models import Order
>>>>>>> 7f806860f1e67defe72020e07a1eb3a4ea72fa32

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['carName', 'carType', 'carDescription', 'carRate']
<<<<<<< HEAD
=======

>>>>>>> 7f806860f1e67defe72020e07a1eb3a4ea72fa32
