"""project_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

# import restaurant_category.urls as restaurant_category
# import order_transaction_courier.urls as order_transaction_courier
# import food_ingredient.urls as food_ingredient


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('example_app.urls')),
    # path('restaurant_category/', include(restaurant_category)),
    # path('order_transaction_courier/', include(order_transaction_courier)),
    # path('food_ingredient/', include(food_ingredient)),
    path('delivery_fee/', include('delivery_fee.urls')),
    path('food/', include('food.urls')),
]
