from django.shortcuts import render

# Create your views here.
def show_admin_dash(request):
    return render(request, "User_Admin_Dashboard.html")

def show_courier_dash(request):
    return render(request, "User_Courier_Dashboard.html")

def show_customer_dash(request):
    return render(request, "User_Customer_Dashboard.html")

def show_restaurant_dash(request):
    return render(request, "User_Restaurant_Dashboard.html")

def show_courier_profile(request):
    return render(request, "User_Courier_Profile.html")

def show_customer_profile(request):
    return render(request, "User_Customer_Profile.html")

def show_restaurant_profile(request):
    return render(request, "User_Restaurant_Profile.html")
