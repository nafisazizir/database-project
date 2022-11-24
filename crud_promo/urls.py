from django.urls import path
from crud_promo.views import show_promos, show_rpromos, min_trans_pform, special_day_pform, special_day_details, min_trans_details, special_edit_details, min_edit_details

app_name = 'crud_promo'

urlpatterns = [
    path('', show_promos, name='show_promos'),
    path('r', show_rpromos, name='show_rpromos'),
    path('new_min', min_trans_pform, name='min_trans_pform'),
    path('new_special', special_day_pform, name='special_day_pform'),
    path('sp_details', special_day_details, name='special_day_details'),
    path('min_details', min_trans_details, name='min_trans_details'),
    path('special_edit', special_edit_details, name='special_edit_details'),
    path('min_edit', min_edit_details, name='min_edit_details'),
]