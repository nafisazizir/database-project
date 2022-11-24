from django.shortcuts import render


def create_order_transaction_customer(request):
    return render(request, "c_order_transaction_customer")


def read_order_transaction_customer(request):
    return render(request, "r_order_transaction_customer")
