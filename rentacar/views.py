from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'RentACar/homepage.html')

def cars(request):
    return render(request, 'RentACar/cars.html')

def about(request):
    return render(request, 'RentACar/about.html')
