from django.urls import path
from .api import subscribe, unsubscribe, get_all_subscribers, get_all_target_users, \
    get_all_subscribers_for_profile_id, get_all_target_users_for_profile_id, \
    is_sub, is_target_user

urlpatterns = [
    # подписаться на пользователя с profile_id
    path('sub/<uuid:target_user_id_profile>/', subscribe, name='subscribe'),

    # отписаться от пользователя с profile_id
    path('unsub/<uuid:target_user_id_profile>/', unsubscribe, name='unsubscribe'),

    # получить все подписки юзера
    path('get_all_sub/', get_all_subscribers, name='get_all_subscribers'),

    # получить всех подписчиков юзера
    path('get_all_target_users/', get_all_target_users, name='get_all_target_users'),

    # получить всех подписчиков пользователя с profile_id
    path('get_all_target_users/<uuid:target_user_id_profile>/', get_all_subscribers_for_profile_id, name='get_all_subscribers_for_profile_id'),

    # получить все подписки пользователя с profile_id
    path('get_all_sub_users/<uuid:target_user_id_profile>/', get_all_target_users_for_profile_id, name='get_all_target_users_for_profile_id'),

    # узнать подписан ли конкретный пользователь с profile_id на юзера
    path('is_sub/<uuid:target_user_id_profile>/', is_sub, name='is_sub'),

    # узнать есть ли конкретный пользователь с profile_id у юзера в подписках
    path('is_target_user/<uuid:target_user_id_profile>/', is_target_user, name='is_target_user'),

]