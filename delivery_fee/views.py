from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers


def show_fee(request):
    return render(request, "R_delivery_fee.html")

def add_fee(request):
    return render(request, "C_delivery_fee.html")

def change_fee(request):
    return render(request, "U_delivery_fee.html")