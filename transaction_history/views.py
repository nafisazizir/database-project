from django.shortcuts import render

# Create your views here.
def show_customers(request):
    return render(request, "customers.html")

def show_couriers(request):
    return render(request, "couriers.html")

def show_restaurants(request):
    return render(request, "restaurants.html")

def show_details(request):
    return render(request, "orderdetails.html")

def show_rating(request):
    return render(request, "rating.html")