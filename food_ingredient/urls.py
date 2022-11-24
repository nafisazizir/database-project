from django.urls import path
from .views import *

app_name = 'food_ingredient'

urlpatterns = [
    path('create_food_ingredient', create_food_ingredient, name = 'create_food_ingredient'),
    path('read_food_ingredient', read_food_ingredient, name = 'read_food_ingredient')
]