from django.urls import path
from .api import get_profile, edit_profile, \
    get_captain_team, get_photo, add_photo, del_photo

urlpatterns = [
    path('<uuid:user_profile_uuid>/', get_profile, name='get_profile'),
    path('edit/<uuid:uuid_profile>/', edit_profile, name='edit_profile'),

    path('<slug:slug_team>/', get_captain_team, name='get_captain_team'),

    path('photos/<uuid:uuid_profile>/', get_photo, name='get_photo'),
    path('add_photos/<uuid:uuid_profile>/', add_photo, name='add_photo'),
    path('del_photo/<uuid:uuid_profile>/', del_photo, name='del_photo')

]
