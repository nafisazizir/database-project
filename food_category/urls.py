from django.urls import path
from .views import *

app_name = "food_category"

urlpatterns = [
    path("create", create_food_category, name="create_food_category"),
    path("", read_food_category, name="read_food_category"),
    path(
        "delete/<food_category_name>", delete_food_category, name="delete_food_category"
    ),
]
