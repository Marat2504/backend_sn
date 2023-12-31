from django.urls import path

from .api import send_track, get_all_tracks, edit_track, del_track


urlpatterns = [
    # отправить на сервер фото с треком
    path('<uuid:user_profile_uuid>/', send_track, name='send_track'),

    # получить все треки пользователя с profile id
    path('tracks/<uuid:user_profile_uuid>/', get_all_tracks, name='get_all_tracks'),

    # изменить данные трека
    path('edit/<int:track_id>/', edit_track, name='edit_track'),

    # изменить данные трека
    path('del/<int:track_id>/', del_track, name='del_track'),
]