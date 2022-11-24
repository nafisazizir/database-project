from django.urls import path
from .views import *

app_name = 'operational_hours'

urlpatterns = [
    path('', read, name='read'),
    path('create', create, name='create'),
    path('update', update, name='update'),
]