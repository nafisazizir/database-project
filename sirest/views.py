from django.shortcuts import render, redirect
from django.db import connection

def homepage(request):
    return render(request, 'homepage.html')

def login_register(request):
    return render(request, 'login_register.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def register_admin(request):
    return render(request, 'register_admin.html')

def register_customer(request):
    return render(request, 'register_customer.html')

def register_restaurant(request):
    return render(request, 'register_restaurant.html')

def register_courier(request):
    return render(request, 'register_courier.html')