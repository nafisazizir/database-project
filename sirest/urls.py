from django.urls import path
from .views import *

app_name = 'sirest'

urlpatterns = [
    path('', homepage, name = 'homepage'),
    path('login_register/', login_register, name = 'login_register'),
    path('login/', login, name = 'login'),
    path('register/', register, name = 'register'),
    path('register_admin/', register_admin, name = 'register_admin'),
    path('register_customer/', register_customer, name = 'register_customer'),
    path('register_restaurant/', register_restaurant, name = 'register_restaurant'),
    path('register_courier/', register_courier, name = 'register_courier'),
]