from django.shortcuts import render


def create_food_category(request):
    return render(request, "c_food_category.html")


def read_food_category(request):
    return render(request, "r_food_category.html")
