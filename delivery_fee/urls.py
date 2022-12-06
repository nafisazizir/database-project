from django.urls import path
from delivery_fee.views import *

app_name = 'delivery_fee'

urlpatterns = [
    path('', show_fee, name='show_fee'),
    path('add_fee/', add_fee, name='add_fee'),
    path('change_fee/', change_fee, name='change_fee'),
    path('delete_fee/<int:id>', delete_fee, name='delete_fee'),
]