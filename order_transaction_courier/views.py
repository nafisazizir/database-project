from django.shortcuts import render


def read_order_transaction_courier(request):
    return render(request, "r_order_transaction_courier.html")


def c_order_transaction_courier(request):
    return render(request, "c_order_transaction_courier.html")
