from django.urls import path
from .views import *

app_name = 'restopay'

urlpatterns = [
    path('restaurant', read_restopay_restaurant, name='read_restopay_restaurant'),
    path('topup_restaurant', topup_restaurant, name='topup_restaurant'),
    path('withdraw_restaurant', withdraw_restaurant, name='withdraw_restaurant'),
    path('customer', read_restopay_customer, name='read_restopay_customer'),
    path('topup_customer', topup_customer, name='topup_customer'),
    path('withdraw_customer', withdraw_customer, name='withdraw_customer'),
    path('courier', read_restopay_courier, name='read_restopay_courier'),
    path('topup_courier', topup_courier, name='topup_courier'),
    path('withdraw_courier', withdraw_courier, name='withdraw_courier'),
]