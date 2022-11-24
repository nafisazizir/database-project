from django import path
from .views import *

app_name = 'restaurant_category'

urlpatterns = [
    path('create_restaurant_category', create_restaurant_category, name = 'create_restaurant_category'),
    path('read_restaurant_category', read_restaurant_category, name = 'read_restaurant_category'),
]