from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
import datetime
from food.models import *

def show_resto_list(request):
    delivery_fee_price = Resto.objects.all()
    context = {
        'list_item': delivery_fee_price,
    }
    return render(request, "R_delivery_fee.html", "R_resto_detail.html" ,context)


def show_food(request):
    food_data = Task.objects.all()
    context = {
        'list_item': food_data,
    }
    return render(request, "R_food_data.html",context)

def add_food(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        description = request.POST.get("desc")
        stock = request.POST.get("stock")
        price = request.POST.get("price")
        fatcat = request.POST.get("fatcat")
        yngvi = request.POST.get("yngvi")
        Task.objects.create(
            user=request.user,
            fname = fname,
            description = description,
            stock = stock,
            price = price,
            fatcat = fatcat,
            yngvi=yngvi,
        )
        return HttpResponseRedirect(reverse("delivery_fee:show_food"))
    return render(request, "C_food_data.html")

def change_food(request):
    if request.method == "PUT":
        task = Task.objects.get(user=request.user, id=id)
        task.save()
        return JsonResponse(
            {
                "pk": task.id,
                "fields": {
                    "fname" : task.fname,
                    "description" : task.description,
                    "stock" : task.stock,
                    "price" : task.price,
                    "fatcat":task.fatcat,
                    "yngvi":task.yngvi,
                },
            },
            status=200,
        )



