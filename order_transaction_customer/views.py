from django.shortcuts import render


def create_order_transaction_customer_1(request):
    return render(request, "c_delivery_address.html")


def create_order_transaction_customer_2(request):
    return render(request, "c_restaurant_selection.html")


def create_order_transaction_customer_3(request):
    return render(request, "c_selection.html")


def create_order_transaction_customer_4(request):
    return render(request, "c_order_list.html")


def create_order_transaction_customer_5(request):
    return render(request, "c_payment_confirmation.html")


def read_order_transaction_customer_1(request):
    return render(request, "r_ongoing_orders.html")


def read_order_transaction_customer_2(request):
    return render(request, "r_order_summary.html")
