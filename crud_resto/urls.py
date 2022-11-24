from django.urls import path
from crud_resto.views import show_restopromos, min_trans_rform, special_day_rform, special_day_rdetails, min_trans_rdetails, special_edit_rdetails, min_edit_rdetails

app_name = 'crud_resto'

urlpatterns = [
    path('', show_restopromos, name='show_restopromos'),
    path('new_min', min_trans_rform, name='min_trans_rform'),
    path('new_special', special_day_rform, name='special_day_rform'),
    path('special_rdetails', special_day_rdetails, name='special_day_rdetails'),
    path('min_rdetails', min_trans_rdetails, name='min_trans_rdetails'),
    path('rspecial_edit', special_edit_rdetails, name='special_edit_rdetails'),
    path('rmin_edit', min_edit_rdetails, name='min_edit_rdetails'),
]