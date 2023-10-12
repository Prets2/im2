from django.http import HttpResponse
from django.shortcuts import render, redirect  # Import the redirect function
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import logout
from django.contrib import messages

def landing_page(request):
    return render(request, 'RentACar/landingpage.html')


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
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if a user with the same username or email already exists
        if User.objects.filter(Q(username=username) | Q(email=email)).exists():
            messages.error(request, 'Username or email already exists.')
            return render(request, 'RentACar/register.html')

        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        user.save()
        return redirect('login')
    return render(request, 'RentACar/register.html')

def home(request):
    return render(request, 'RentACar/homepage.html')

def logout_view(request):
    logout(request)
    return redirect('login')
