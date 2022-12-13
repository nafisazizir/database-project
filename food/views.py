import random
import string
from django.db import connection
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def show_resto_list(request):
    SQL = f"""
    SELECT rname,rbranch,rating
    FROM RESTAURANT
    """
    return render(request, "R_resto_list.html")

def show_resto_detail(request):
    SQL = f"""
    SELECT *
    FROM RESTAURANT
    """
    return render(request, "R_resto_detail.html")

def show_food(request):
    SQL = f"""
    SELECT *
    FROM FOOD
    """
    return render(request, "R_food_data.html")

def add_food(request):
    if not request.session.get("isLoggedIn"):
        return redirect('sirest:logout')
    if not request.session.get("role") == 'admin':
        return redirect('sirest:logout')

    def varcharRandomizer():
        characters = string.ascii_letters + string.digits
        varchar = ''.join(random.choice(characters) for i in range(random.randint(6,9)))
        return varchar
    errors = []
    cursor = connection.cursor()
    cursor.execute("SET search_path to SIREST")
    
    if request.method == "POST":
        fname = request.POST.get('fname')
        desc = request.POST.get('desc')
        stock = request.POST.get('stock')
        price = request.POST.get('price')
        fatcat = request.POST.get('fatcat')
        yngvi = request.POST.get('yngvi')

        SQL = f"""
        SELECT foodname
        FROM DELIVERY_FEE_PER_KM
        """

        cursor.execute(SQL)
        id_tuple = [i[0].strip() for i in cursor.fetchall()]

        id = varcharRandomizer()

        while id in id_tuple:
            id = varcharRandomizer()

        if fname and desc and stock and price and fatcat and yngvi:
            SQL = f"""
            INSERT food
            VALUES 
            ('{id}', '{fname}', '{desc}', '{stock}','{price}','{fatcat}','{yngvi}')
            """
            cursor.execute(SQL)
            return redirect('food:show_food')

        else:
            errors.append("Please fill out all fields.")

    return render(request,"C_food_data.html", {'errors': errors})

def change_food(request):
    if not request.session.get("isLoggedIn"):
        return redirect('sirest:logout')
    if not request.session.get("role") == 'admin':
        return redirect('sirest:logout')
    # if request.method == "PUT":
    #     task = Task.objects.get(user=request.user, id=id)
    #     task.save()
    #     return JsonResponse(
    #         {
    #             "pk": task.id,
    #             "fields": {
    #                 "fname" : task.fname,
    #                 "description" : task.description,
    #                 "stock" : task.stock,
    #                 "price" : task.price,
    #                 "fatcat":task.fatcat,
    #                 "yngvi":task.yngvi,
    #             },
    #         },
    #         status=200,
    #     )
    return render(request, "U_food_data.html")


