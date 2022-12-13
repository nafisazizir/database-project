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
from django.db import connection
from django.views.decorators.csrf import csrf_exempt

def show_fee(request):
    if not request.session.get("isLoggedIn"):
        return redirect('sirest:logout')
    if not request.session.get("role") == 'admin':
        return redirect('sirest:logout')
    cursor = connection.cursor()
    cursor.execute("SET search_path to PUBLIC")
    email = request.session.get('user_email')
    cursor.execute("SET search_path to SIREST")
    SQL = f"""
    SELECT *
    FROM DELIVERY_FEE_PER_KM;
    """
    cursor.execute(SQL)
    delivery_fee_per_km = cursor.fetchall()

    context = {
        'delivery_fee': delivery_fee_per_km,
    }

    return render(request, "R_delivery_fee.html", context)

@csrf_exempt
def add_fee(request):
    if not request.session.get("isLoggedIn"):
        return redirect('sirest:logout')
    if not request.session.get("role") == 'admin':
        return redirect('sirest:logout')

    cursor = connection.cursor()
    cursor.execute("SET search_path to SIREST")
    
    if request.method == "POST":
        province = request.POST.get('province')
        motorate= request.POST.get('motorate')
        carrate = request.POST.get('carrate')
        SQL = f"""
        SELECT MAX(CAST(Id AS NUMERIC))
        FROM DELIVERY_FEE_PER_KM;
        """

        cursor.execute(SQL)
        id = cursor.fetchone()

        newid = 1
        if id[0]:
            newid = int(id[0]) + 1

        if province and motorate and carrate:
            SQL = f"""
            INSERT INTO DELIVERY_FEE_PER_KM
            VALUES 
            ('{newid}', '{province}', '{motorate}', '{carrate}');
            """
            cursor.execute(SQL)
            return redirect('delivery_fee:show_fee')


    return render(request, "C_delivery_fee.html",)

@csrf_exempt
def change_fee(request, province, motorfee, carfee):
    if not request.session.get("isLoggedIn"):
        return redirect('sirest:logout')
    if not request.session.get("role") == 'admin':
        return redirect('sirest:logout')

    cursor = connection.cursor()
    cursor.execute("SET search_path to PUBLIC")
    email = request.session.get('user_email')
    cursor.execute("SET search_path to SIREST")

    if request.method == "POST":
        motorate = request.POST.get('motorate')
        carrate = request.POST.get('carrate')
        if motorate and carrate:
            SQL = f"""
            UPDATE DELIVERY_FEE_PER_KM
            SET motorfee = '{motorate}', carfee = '{carrate}'
            WHERE id = '{id}' AND province = '{province}' AND motorfee = '{motorfee}' AND carfee = '{carfee}';
            """
        cursor.execute(SQL)
        return redirect('delivery_fee:show_fee')

    SQL = f"""
    SELECT id
    FROM DELIVERY_FEE_PER_KM
    WHERE province = '{province}' AND motorfee = '{motorfee}' AND carfee = '{carfee}';
    """
    cursor.execute(SQL)

    id = cursor.fetchone()[0]
    print(id)
        
    context = {
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
        WHERE province = '{province}' AND motorfee = '{motorfee}' AND carfee = '{carfee}';
        """
    cursor.execute(SQL)

    return redirect('delivery_fee:show_fee')
