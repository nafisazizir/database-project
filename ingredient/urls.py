from django.urls import path
from .views import *

app_name = 'ingredient'

urlpatterns = [
    path('create', create_ingredient, name = 'c_ingredient'),
    path('', read_ingredient, name = 'r_ingredient'),
    path('delete_ingredient/<ingredient_name>', delete_ingredient, name = 'delete_ingredient')
]