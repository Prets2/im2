from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


def landing_page(request):
    return render(request, 'RentACar/landingpage.html')

def home(request):
    return render(request, 'RentACar/homepage.html')

def cars(request):
    return render(request, 'RentACar/cars.html')

def about(request):
    return render(request, 'RentACar/about.html')

class CustomLoginView(LoginView):
    template_name = 'RentACar/login.html'  # Your login template
    redirect_authenticated_user = True  # Redirect authenticated users away from login page
    success_url = reverse_lazy('homepage')  # Specify the URL to redirect to upon successful login

    def get_success_url(self):
        return self.success_url