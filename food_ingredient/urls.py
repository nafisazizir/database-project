from django.urls import path
from .views import *

app_name = 'food_ingredient'

urlpatterns = [
    path('create', create_food_ingredient, name = 'c_food_ingredient'),
    path('', read_food_ingredient, name = 'r_food_ingredient')
]