# forms.py

from django import forms
from .models import Car
<<<<<<< HEAD
=======
from .models import Order
>>>>>>> 34664579a4e00b00abb7c1763225365abe193a20

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
<<<<<<< HEAD
        fields = ['carName', 'carType', 'carDescription', 'carRate']
=======
        fields = ['carName', 'carType', 'carDescription', 'carRate', 'carPic']

>>>>>>> 34664579a4e00b00abb7c1763225365abe193a20
