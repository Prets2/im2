from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login


def landing_page(request):
    return render(request, 'RentACar/landingpage.html')

def home(request):
    return render(request, 'RentACar/homepage.html')

def cars(request):
    return render(request, 'RentACar/cars.html')

def about(request):
    return render(request, 'RentACar/about.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or another page
            return redirect('home')
        else:
            # Return an error message or handle the failed login attempt
            pass
    return render(request, 'login.html')