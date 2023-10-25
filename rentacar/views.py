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
from django.http import JsonResponse
from .models import Car, Order
from django.shortcuts import render, get_object_or_404
from django.forms import ModelForm
<<<<<<< HEAD
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import uuid
import random
import string

def create_order(request):
    if request.method == 'POST':
        car_id = request.POST.get('carID')
        start_date = request.POST.get('startDate')
        end_date = request.POST.get('endDate')
        duration = request.POST.get('duration')

        # Calculate the total price based on car rate and duration
        car = get_object_or_404(Car,car_id)
        total = 1000
        order_number = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
        

        # Create the Order instance
        order = Order(
            orderNumber=order_number,
            userid=request.user,  # Assuming you have a logged-in user
            carid=car.CarID,
            carName=car.carName,
            startDate=start_date,
            endDate=end_date,
            total=total,
            duration=duration
        )

        order.save()

        return JsonResponse({'success': True, 'message': 'Order created successfully'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})
        
def generate_unique_order_number():
    # Generate a unique order number using a UUID
    order_number = str(uuid.uuid4()).replace("-", "")[
        :8
    ]  # You can adjust the length as needed
    return order_number

=======
from .forms import CarForm
>>>>>>> f286d568a705ede3bc90013470a0f6c7900b81b4

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
        "user_is_admin": user_is_admin,
    }
    return render(request, "RentACar/carman.html", context)

=======
        'user_is_admin': user_is_admin,
        'cars': cars,  # Pass the list of cars to the template
    }
    return render(request, "RentACar/carman.html", context)
>>>>>>> f286d568a705ede3bc90013470a0f6c7900b81b4

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


@login_required
def add_car(request):
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("car_management")
    else:
        form = CarForm()
<<<<<<< HEAD

    return render(request, "add_car.html", {"form": form})


@login_required
def edit_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == "POST":
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect("car_management")
    else:
        form = CarForm(instance=car)

    return render(request, "edit_car.html", {"form": form})


@login_required
def delete_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == "POST":
        car.delete()
        return redirect("car_management")

    return render(request, "delete_car.html", {"car": car})
=======
    return render(request, 'RentACar/add_car.html', {'form': form})
>>>>>>> f286d568a705ede3bc90013470a0f6c7900b81b4
