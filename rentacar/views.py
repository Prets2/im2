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
from .models import Car
from django.shortcuts import render, get_object_or_404

def get_username(request):
    if request.user.is_authenticated:
        username = request.user.username
        return JsonResponse({'username': username})
    else:
        return JsonResponse({'error': 'User not authenticated'})
    
def landing_page(request):
    return render(request, "RentACar/landingpage.html")

def home(request):
    user_is_admin = request.user.is_staff

    context = {
        'user_is_admin': user_is_admin,
    }
    return render(request, "RentACar/homepage.html",context)

def viosfinal(request):
    # Add your logic for the 'viosfinal' view here
    return render(request, "RentACar/viosfinal.html")

def ertigafinal(request):
    # Add your logic for the 'viosfinal' view here
    return render(request, "RentACar/ertigafinal.html")


def terms_and_conditions(request):
    return render(request, "RentACar/terms_and_conditions.html")


def cars(request):
    car = Car.objects.all()
    return render(request, "RentACar/car_list.html", {'cars': car} )


def about(request):
    return render(request, "RentACar/about.html")


@login_required
def carlists(request):
    # Your carlists view logic goes here
    return render(request, "RentACar/login.html")

def cart(request, car_id):
    car = get_object_or_404(Car, CarID=car_id)
    return render(request, "RentACar/cart.html", {'car': car})

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
    return render(request, "RentACar/car_detail.html", {'car': car})    

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
