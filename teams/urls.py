from django.urls import path
from .api import get_teams, is_subscribe, create_team, get_current_team, \
    get_current_team_athletes, edit_current_team

urlpatterns = [
    path('', get_teams, name='get_teams'),
    path('<uuid:user_id>/', get_teams, name='get_teams'),

    path('<uuid:team_id>/<uuid:user_id>/', is_subscribe, name='is_subscribe'),

    path('create/', create_team, name='create_team'),

    path('edit/<uuid:team_uuid>/<uuid:user_uuid>/', edit_current_team, name='edit_current_team'),

    path('<slug:slug_team>/', get_current_team, name='get_current_team'),
    path('<slug:slug_team>/athletes/', get_current_team_athletes, name='get_current_team_athletes'),

]


