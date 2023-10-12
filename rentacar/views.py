from django.http import HttpResponse
from django.shortcuts import render, redirect  # Import the redirect function
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages

def landing_page(request):
    return render(request, 'RentACar/landingpage.html')

def home(request):
    return render(request, 'RentACar/homepage.html')

def cars(request):
    return render(request, 'RentACar/cars.html')

def about(request):
    return render(request, 'RentACar/about.html')

class CustomLoginView(LoginView):
    template_name = 'RentACar/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('homepage')  # Redirect to the homepage

    def get_success_url(self):
        return self.success_url



def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
        user.save()
        return redirect('login')
    return render(request, 'RentACar/register.html')