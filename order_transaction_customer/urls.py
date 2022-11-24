from django.urls import path
from .views import *

app_name = "order_transaction_customer"

urlpatterns = [
    path(
        "create_order_transaction_customer",
        create_order_transaction_customer,
        name="create_order_transaction_customer",
    ),
    path(
        "read_order_transaction_customer",
        read_order_transaction_customer,
        name="read_order_transaction_customer",
    ),
]
