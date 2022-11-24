from django.urls import path
from .views import *

app_name = 'order_transaction_courier'

urlpatterns = [
    path('', read_order_transaction_courier, name = 'r_oder_transaction_courier'),
    path('summary', summary_order_transaction_courier, name = 'summary_order_transaction_courier')
]