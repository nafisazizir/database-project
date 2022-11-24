from django.urls import path
from .views import *

app_name = 'order_transaction_courier'

urlpatterns = [
    path('r_oder_transaction_courier', read_order_transaction_courier, name = 'r_oder_transaction_courier'),
    path('summary_order_transaction_courier', summary_order_transaction_courier, name = 'summary_order_transaction_courier')
]