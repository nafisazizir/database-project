from django.urls import path
from .views import *

app_name = "order_transaction_courier"

urlpatterns = [
    path('', read_order_transaction_courier, name = 'ongoing_order'),
    path('summary/<restaurant_branch>', summary_order_transaction_courier, name = 'summary')
]
