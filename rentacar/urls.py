from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('home', views.home, name='home'),
    path('cars/', views.cars, name='cars'),
    path('about/', views.about, name='about'),
    path('login/', views.login_view, name='login'),
]
