from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('home', views.home, name='home'),
    path('cars/', views.cars, name='cars'),
    path('cars/viosfinal', views.viosfinal, name='viosfinal'),  # Nested under 'cars/'
    path('about/', views.about, name='about'),
    path('login/', LoginView.as_view(template_name='RentACar/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('terms_and_conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    path('send_email/', views.send_email, name='send_email'),
]
