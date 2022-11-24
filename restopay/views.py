from django.shortcuts import render

def read_restopay(request):
    return render(request, "read_restopay.html")

def topup(request):
    return render(request, "update_topup.html")

def withdraw(request):
    return render(request, "update_withdraw.html")
