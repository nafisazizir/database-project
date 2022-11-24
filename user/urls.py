from django.urls import path
from user.views import show_admin_dash, show_courier_dash, show_courier_profile, show_customer_dash, show_customer_profile, show_restaurant_dash, show_restaurant_profile
app_name = 'user'

urlpatterns = [
    path('admin', show_admin_dash, name='show_admin_dash'),
    path('courier', show_courier_dash, name='show_courier_dash'),
    path('courier_profile', show_courier_profile, name='show_courier_profile'),
    path('customer', show_customer_dash, name='show_customer_dash'),
    path('customer_profile', show_customer_profile, name='show_customer_profile'),
    path('restaurant', show_restaurant_dash, name='show_restaurant_dash'),
    path('restaurant_profile', show_restaurant_profile, name='show_restaurant_profile'),
]