from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
import datetime
# from delivery_fee.models import Task


def show_fee(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path to SIREST;")
    SQL = f"""
    SELECT * FROM DELIVERY_FEE_PER_KM
    """
    cursor.execute(SQL)
    alldeliveryfee = cursor.fetchall()

    context = {'deliveryfee': alldeliveryfee}
    return render(request, 'R_delivery_fee.html', context)

def add_fee(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path to SIREST;")

    if request.method == 'POST':
        id = request.POST.get('id')
        province = request.POST.get('province')
        motorfee = request.POST.get('motorfee')
        carfee = request.POST.get('carfee')
        
    if not id or not province or not motorfee or not carfee:
        return ()
    else:
        newdeliveryfeeperkm = (id, province, motorfee, carfee)
        SQL = f"""
        INSERT INTO DELIVERY_FEE_PER_KM VALUES {newdeliveryfeeperkm}
        """
        cursor.execute(SQL)
    return redirect('delivery_fee:show_fee')

def change_fee(request):
#     if request.method == "PUT":
#         task = Task.objects.get(user=request.user, id=id)
#         task.save()
#         return JsonResponse(
#             {
#                 "pk": task.id,
#                 "fields": {
#                     "province": task.province,
#                     "motorate": task.motorate,
#                     "carrate": task.carrate,
#                 },
#             },
#             status=200,
#         )
    return render(request, "U_delivery_fee.html")

def delete_fee(request, id):
    cursor = connection.cursor()
    cursor.execute("SET search_path to SIREST;")

    SQL = f"""
    SELECT EXISTS (SELECT * FROM DELIVERY_FEE_PER_KM WHERE id = '{id}')
    """
    cursor.execute(SQL)

    isitthere = cursor.fetchone()[0]
    if isitthere:
        SQL = f"""
        DELETE FROM DELIVERY_FEE_PER_KM WHERE id = '{id}'
        """
        cursor.execute(SQL)

    return redirect('delivery_fee:show_fee')
