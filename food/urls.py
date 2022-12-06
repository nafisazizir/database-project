from django.urls import path
from food.views import *

app_name = 'food'

urlpatterns = [
    path('', show_resto_list, name='show_resto_list'),
    path('menu/', show_food, name='show_food'),
    path('add_food/', add_food, name='add_food'),
    path('change_food/', change_food, name='change_food'),
]