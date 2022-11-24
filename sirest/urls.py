from django.urls import path
from .views import *

app_name = 'sirest'

urlpatterns = [
    path('', homepage, name = 'homepage'),
]