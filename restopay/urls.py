from django.urls import path
from .views import *

app_name = 'restopay'

urlpatterns = [
    path('', read_restopay, name='read_restopay'),
    path('topup', topup, name='topup'),
    path('withdraw', withdraw, name='withdraw'),
]