from django.urls import path
from .views import *

app_name = "order_transaction_courier"

urlpatterns = [
    path("", read_order_transaction_courier, name="r_oder_transaction_courier"),
    path("create", c_order_transaction_courier, name="c_order_transaction_courier"),
]
