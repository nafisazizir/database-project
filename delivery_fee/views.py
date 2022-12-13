import random
import string
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
import datetime
from django.db import connection
# from delivery_fee.models import Task


def show_fee(request):
    errors = []
    cursor = connection.cursor()
    cursor.execute("SET search_path to PUBLIC")
    email = request.session.get('user_email')
    cursor.execute("SET search_path to SIREST")
    SQL = f"""
    SELECT province, motorfee, carfee
    FROM DELIVERY_FEE_PER_KM
    """
    cursor.execute(SQL)
    delivery_fee_per_km = cursor.fetchall()

    index = 0
    delivery_fee_per_km_formatted= []
    for stuff in delivery_fee_per_km:
        index += 1
        delivery_fee_per_km_formatted.append((index, stuff[0], stuff[1], stuff[2]))

    context = {
        'errors': errors,
        'delivery_fee': delivery_fee_per_km_formatted,
    }

    return render(request, "R_delivery_fee.html", context)

def add_fee(request):
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
        province = request.POST.get('province')
        motorate= request.POST.get('motorate')
        carrate = request.POST.get('carrate')
        SQL = f"""
        SELECT id
        FROM DELIVERY_FEE_PER_KM
        """

        cursor.execute(SQL)
        id_tuple = [i[0].strip() for i in cursor.fetchall()]

        id = varcharRandomizer()

        while id in id_tuple:
            id = varcharRandomizer()

        if province and motorate and carrate:
            SQL = f"""
            INSERT INTO DELIVERY_FEE_PER_KM
            VALUES 
            ('{id}', '{province}', '{motorate}', '{carrate}')
            """
            cursor.execute(SQL)
            return redirect('delivery_fee:show_fee')

        else:
            errors.append("Please fill every field")

    return render(request, "C_delivery_fee.html", {'errors': errors})

def change_fee(request, province, motorfee, carfee):
    if not request.session.get("isLoggedIn"):
        return redirect('sirest:logout')
    if not request.session.get("role") == 'admin':
        return redirect('sirest:logout')

    errors = []
    cursor = connection.cursor()
    cursor.execute("SET search_path to PUBLIC")
    email = request.session.get('user_email')
    cursor.execute("SET search_path to SIREST")

    if request.method == "POST":
        motorate = request.POST.get('motorate')
        carrate = request.POST.get('carrate')

        if new_motorfee and new_carfee:
            SQL = f"""
            SELECT *
            FROM DELIVERY_FEE_PER_KM
            WHERE province = '{province}' AND motorfee = '{motorfee}' AND carfee = '{carfee}'
            """
            cursor.execute(SQL)

            id = cursor.fetchone()[0]
            print(id)

            try:
                SQL = f"""
                UPDATE DELIVERY_FEE_PER_KM
                SET motorfee = '{motorate}', carfee = '{carrate}'
                WHERE id = '{id}' AND province = '{province}' AND motorfee = '{motorfee}' AND carfee = '{carfee}'
                """
                cursor.execute(SQL)

                return redirect('delivery_fee:show_fee')

            except:
                errors.append("Chosen fee does not exist")
        
        else:
            errors.append("Please fill all the fields")

    context = {
        'errors': errors,
        'province': province,
        'motorfee': motorfee,
        'carfee': carfee,
    }

    return render(request, "U_delivery_fee.html", context)

def delete_fee(request, province, motorfee, carfee):
    if not request.session.get("isLoggedIn"):
        return redirect('sirest:logout')
    if not request.session.get("role") == 'admin':
        return redirect('sirest:logout')
    cursor = connection.cursor()

    cursor.execute("SET search_path to SIREST")

    SQL = f"""
        DELETE FROM DELIVERY_FEE_PER_KM
        WHERE province = '{province}' AND motorfee = '{motorfee}' AND carfee = '{carfee}'
        """
    cursor.execute(SQL)

    return redirect('delivery_fee:show_fee')
