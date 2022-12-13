from django.urls import path
from .views import *

app_name = "order_transaction_customer"

urlpatterns = [
    path(
        "",
        create_order_transaction_customer_1,
        name="order1",
    ),
    path(
        "restaurant",
        create_order_transaction_customer_2,
        name="order2",
    ),
    path(
        "select",
        create_order_transaction_customer_3,
        name="order3",
    ),
    path(
        "payment",
        create_order_transaction_customer_4,
        name="order4",
    ),
    path(
        "confirm",
        create_order_transaction_customer_5,
        name="order5",
    ),
    path(
        "orders",
        read_order_transaction_customer_1,
        name="read_order1",
    ),
    path(
        "order-summary",
        read_order_transaction_customer_2,
        name="read_order2",
    ),
]
