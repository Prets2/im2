from urllib import response
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import logout
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import render
from .models import Car, Order
from django.shortcuts import render, get_object_or_404
from django.forms import ModelForm
<<<<<<< HEAD
=======
from django.http import JsonResponse
>>>>>>> 4641a7022ab12a3603091b466135ef00958786cf
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Order, Car
from django.shortcuts import render, redirect, get_object_or_404
import random
import string
import json

@csrf_exempt
def create_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        car_id = data['carID']
        start_date = data['startDate']
        end_date = data['endDate']
        duration = data['duration']

        # Retrieve the Car object
        car = Car.objects.get(pk=car_id)

        # Generate a random order number
        order_number = ''.join(random.choices(string.digits, k=8))

        # Calculate the total (replace this with your own logic)
        total = car.carRate * float(duration)

        # Create the Order object
        order = Order.objects.create(
            orderNumber=order_number,
            userid=request.user,
            carid=car,
            carName=car.carName,
            startDate=start_date,
            endDate=end_date,
            total=total,
            duration=duration,
        )

        car.status = 1
        car.save()
        
        return JsonResponse({'success': True, 'orderNumber': order.orderNumber})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})

<<<<<<< HEAD
=======

from django.shortcuts import render, redirect
>>>>>>> 4641a7022ab12a3603091b466135ef00958786cf
from .forms import CarForm

def get_username(request):
    if request.user.is_authenticated:
        username = request.user.username
        return JsonResponse({"username": username})
    else:
        return JsonResponse({"error": "User not authenticated"})


def landing_page(request):
    return render(request, "RentACar/landingpage.html")


def home(request):
    user_is_admin = request.user.is_staff

    context = {
        "user_is_admin": user_is_admin,
    }
    return render(request, "RentACar/homepage.html", context)


def viosfinal(request):
    # Add your logic for the 'viosfinal' view here
    return render(request, "RentACar/viosfinal.html")


def ertigafinal(request):
    # Add your logic for the 'viosfinal' view here
    return render(request, "RentACar/ertigafinal.html")


def terms_and_conditions(request):
    return render(request, "RentACar/terms_and_conditions.html")


def car_management(request):
    # Check if the user is an admin
    user_is_admin = request.user.is_staff
    # Fetch the list of cars from the database
    cars = Car.objects.all()
    context = {
<<<<<<< HEAD
        'user_is_admin': user_is_admin,
        'cars': cars,  # Pass the list of cars to the template
    }
    return render(request, "RentACar/carman.html", context)
=======
        "user_is_admin": user_is_admin,
        "cars": cars,  # Add the 'cars' context variable
    }
    return render(request, "RentACar/carman.html", context)

>>>>>>> 4641a7022ab12a3603091b466135ef00958786cf

def cars(request):
    car = Car.objects.all()
    return render(request, "RentACar/car_list.html", {"cars": car})


def about(request):
    return render(request, "RentACar/about.html")


@login_required
def carlists(request):
    return render(request, "RentACar/login.html")


def cart(request, car_id):
    car = get_object_or_404(Car, CarID=car_id)
    return render(request, "RentACar/cart.html", {"car": car})


class CustomLoginView(LoginView):
    template_name = "RentACar/login.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy("homepage")

    def get_success_url(self):
        return self.success_url

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password. Please try again.")
        return super().form_invalid(form)


def car_detail(request, car_id):
    car = get_object_or_404(Car, CarID=car_id)
    return render(request, "RentACar/car_detail.html", {"car": car})


def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(Q(username=username) | Q(email=email)).exists():
            messages.error(request, "Username or email already exists.")
            return render(request, "RentACar/register.html")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.save()
        return redirect("login")
    return render(request, "RentACar/register.html")


def logout_view(request):
    logout(request)
    return redirect("login")


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ["carName", "carType", "carDescription", "carRate"]


from .forms import CarForm  # Import the CarForm

from django.shortcuts import render, get_object_or_404, redirect
from .models import Car
from .forms import CarForm

@login_required
def add_car(request):
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)  # Create a car object but don't save it yet
            car.save()  # Save the car object to generate a CarID
            # Handle the image file upload
            if 'carImage' in request.FILES:
                car.carPic = request.FILES['carImage']
                car.save()
            return redirect("car_management")
    else:
        form = CarForm()

    return render(request, "RentACar/add_car.html", {"form": form})



def update_car(request, car_id):
    # Retrieve the car object from the database
    car = get_object_or_404(Car, CarID=car_id)

    if request.method == "POST":
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            car = form.save()  # Save the updated data to the database

            # Update availability (status) based on the form's status field
            if 'status' in form.cleaned_data:
                car.status = 0 if form.cleaned_data['status'] == 0 else 1
                car.save()

            return redirect('car_management')  # Redirect to the car management page

    else:
        form = CarForm(instance=car)

    context = {
        'form': form,
        'car': car,
    }
    return render(request, 'RentACar/update_car.html', context)


def delete_car(request, car_id):
<<<<<<< HEAD
    car = get_object_or_404(Car, id=car_id)
    if request.method == "POST":
        car.delete()
        return redirect("car_management")

    return render(request, "delete_car.html", {"car": car})
=======
    car = get_object_or_404(Car, pk=car_id)
    car.delete()
    return redirect('car_management')
>>>>>>> 4641a7022ab12a3603091b466135ef00958786cf
