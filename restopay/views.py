from django.shortcuts import render

def read_restopay_restaurant(request):
    return render(request, "read_restopay_restaurant.html")

def topup_restaurant(request):
    return render(request, "update_topup_restaurant.html")

def withdraw_restaurant(request):
    return render(request, "update_withdraw_restaurant.html")

def read_restopay_customer(request):
    return render(request, "read_restopay_customer.html")

def topup_customer(request):
    return render(request, "update_topup_customer.html")

def withdraw_customer(request):
    return render(request, "update_withdraw_customer.html")

def read_restopay_courier(request):
    return render(request, "read_restopay_courier.html")

def topup_courier(request):
    return render(request, "update_topup_courier.html")

def withdraw_courier(request):
    return render(request, "update_withdraw_courier.html")
