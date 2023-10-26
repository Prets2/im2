from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.conf import settings
from django.conf.urls.static import static


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
    path('cart/<int:car_id>/', views.cart, name='cart'),
    path('carman.html', views.car_management, name='car_management'),
    path('car/add/', views.add_car, name='add_car'),
    path('update_car/<int:car_id>/', views.update_car, name='update_car'),
    path('delete_car/<int:car_id>/', views.delete_car, name='delete_car'),
    path('create_order/', views.create_order, name='create_order'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)