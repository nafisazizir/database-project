from django.urls import path
from .views import *

app_name = 'transaction_restaurant'

urlpatterns = [
    path('', read_transaction, name='read_transaction'),
    path('details/<str:custEmail>/<str:timestamp>/<str:rname>/<str:rbranch>', details, name='details'),
]