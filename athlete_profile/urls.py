from django.urls import path
from .api import get_profile, edit_profile, get_captain_team

urlpatterns = [
    path('<uuid:uuid_profile>/', get_profile, name='get_profile'),
    path('edit/<uuid:uuid_profile>/', edit_profile, name='edit_profile'),

    path('<slug:slug_team>/', get_captain_team, name='get_captain_team'),
]
