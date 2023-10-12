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

def landing_page(request):
    return render(request, "RentACar/landingpage.html")


def viosfinal(request):
    # Add your logic for the 'viosfinal' view here
    return render(request, "RentACar/viosfinal.html")


def terms_and_conditions(request):
    return render(request, "RentACar/terms_and_conditions.html")


def cars(request):
    return render(request, "RentACar/cars.html")


def about(request):
    return render(request, "RentACar/about.html")

def send_confirmation_email(request):
    subject = 'Confirmation Email'
    message = 'Thank you for renting with us. Please find your receipt attached.'
    from_email = 'your-email@example.com'  # Sender's email
    recipient_list = [request.user.email]  # Recipient's email

    send_mail(subject, message, from_email, recipient_list, fail_silently=False)



# Add the carlists view here
def carlists(request):
    # Your carlists view logic goes here
    return render(request, "RentACar/carlists.html")


@login_required
def carlists(request):
    # Your carlists view logic goes here
    return render(request, "RentACar/login.html")


class CustomLoginView(LoginView):
    template_name = "RentACar/login.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy("homepage")

    def get_success_url(self):
        return self.success_url

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password. Please try again.")
        return super().form_invalid(form)


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


def home(request):
    return render(request, "RentACar/homepage.html")


def logout_view(request):
    logout(request)
    return redirect("login")
