from django.urls import path
from .views import *

app_name = 'transaction_restaurant'

urlpatterns = [
    path('', read_transaction, name='read_transaction'),
    path('details', details, name='details'),
]