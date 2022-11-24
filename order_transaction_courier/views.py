from django.shortcuts import render

def read_order_transaction_courier(request):
    return render(request, 'r_order_transaction_courier')

def summary_order_transaction_courier(request):
    return render(request, 'summary_transaction_courier')