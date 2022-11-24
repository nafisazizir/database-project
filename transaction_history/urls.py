from django.urls import path
from transaction_history.views import show_customers, show_couriers, show_restaurants, show_details, show_rating

app_name = 'transaction_history'

urlpatterns = [
    path('customers', show_customers, name='show_customers'),
    path('couriers', show_couriers, name='show_couriers'),
    path('restaurants', show_restaurants, name='show_restaurants'),
    path('details', show_details, name='show_details'),
    path('rating', show_rating, name='show_rating'),
]