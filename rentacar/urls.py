from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('home', views.home, name='home'),
    path('cars', views.cars, name='cars'),
    path('about/', views.about, name='about'),
    path('login/', LoginView.as_view(template_name='RentACar/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('terms_and_conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    path('api/get-username/', views.get_username, name='get-username'),
    path('cars/<int:car_id>/', views.car_detail, name='car_detail'),
    path('carman.html', views.car_management, name='car_management'),
    path('car/add/', views.add_car, name='add_car'),
    path('car/edit/<int:car_id>/', views.edit_car, name='edit_car'),
    path('car/delete/<int:car_id>/', views.delete_car, name='delete_car'),
]

