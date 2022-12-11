from django.urls import path
from .views import *

app_name = 'restaurant_category'

urlpatterns = [
    path('create', create_restaurant_category, name = 'create_restaurant_category'),
    path('', read_restaurant_category, name = 'read_restaurant_category'),
    path('delete/str:name', delete_restaurant_category, name = 'delete_category')
]