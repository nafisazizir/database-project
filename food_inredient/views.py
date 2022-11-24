from django.shortcuts import render

def create_food_ingredient(request):
    return render(request, 'c_food_ingredient')

def read_food_ingredient(request):
    return render(request, 'r_food_ingredient')