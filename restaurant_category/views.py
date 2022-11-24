from django.shortcuts import render

def create_restaurant_category(request):
    return render(request, 'c_restaurant_category.html')

def read_restaurant_category(request):
    return render(request, 'r_restaurant_category.html')