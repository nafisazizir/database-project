from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers


def show_resto_list(request):
    return render(request, "R_resto_list.html")

def show_resto_detail(request):
    return render(request, "R_resto_detail.html")

def show_food(request):
    return render(request, "R_food_data.html")

def add_food(request):
    return render(request, "C_food_data.html")

def change_food(request):
    return render(request, "U_food_data.html")



