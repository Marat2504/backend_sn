from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from athlete_profile.models import Profile
from account.models import User
from .models import Subscription

from .serializers import SubscriptionSerializer


# подписаться на пользователя с profile_id
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def subscribe(request, target_user_id_profile):
    subscriber = User.objects.get(id=request.user.id).user_profile
    target_user = Profile.objects.get(id=target_user_id_profile)

    if Subscription.objects.filter(subscriber=subscriber, target_user=target_user).exists():
        return Response({'error': f'{subscriber} уже подписан на {target_user}'})
    else:
        new_sub = Subscription.objects.create(subscriber=subscriber, target_user=target_user)
        new_sub.save()
    serializer = SubscriptionSerializer(new_sub)
    return Response(serializer.data)


# отписаться от пользователя с profile_id
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unsubscribe(request, target_user_id_profile):
    subscriber = User.objects.get(id=request.user.id).user_profile
    target_user = Profile.objects.get(id=target_user_id_profile)

    sub = Subscription.objects.filter(subscriber=subscriber, target_user=target_user)
    if sub.exists():
        serializer = SubscriptionSerializer(sub.first())
        sub.first().delete()
        return Response(serializer.data)
    else:
        return Response({'error', f'{subscriber} не был подписан на {target_user}'})


# получить все подписки юзера
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_all_subscribers(request):
    profile = User.objects.get(id=request.user.id).user_profile
    # все на кого подписан юзер
    all_subscriber = Subscription.objects.filter(subscriber=profile)

    serializer = SubscriptionSerializer(all_subscriber, many=True)
    return Response(serializer.data)


# получить всех подписчиков юзера
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_all_target_users(request):
    profile = User.objects.get(id=request.user.id).user_profile
    # все кто являются подписчиками юзера
    all_target_user = Subscription.objects.filter(target_user=profile)

    serializer = SubscriptionSerializer(all_target_user, many=True)
    return Response(serializer.data)


# получить всех подписчиков пользователя с profile_id
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_all_subscribers_for_profile_id(request, target_user_id_profile):
    profile = Profile.objects.get(id=target_user_id_profile)
    # все кто подписан на конкретного пользователя
    all_target_user = Subscription.objects.filter(target_user=profile)

    serializer = SubscriptionSerializer(all_target_user, many=True)
    return Response(serializer.data)


# получить все подписки пользователя с profile_id
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_all_target_users_for_profile_id(request, target_user_id_profile):
    profile = Profile.objects.get(id=target_user_id_profile)
    # все на кого подписан конкретный пользователь
    all_subscriber = Subscription.objects.filter(subscriber=profile)

    serializer = SubscriptionSerializer(all_subscriber, many=True)
    return Response(serializer.data)


# узнать подписан ли конкретный пользователь с profile_id на юзера
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def is_sub(request, target_user_id_profile):
    profile = Profile.objects.get(id=target_user_id_profile)
    user = User.objects.get(id=request.user.id).user_profile
    # юзер подписан на пользователя с profile_id
    all_subscriber = Subscription.objects.filter(subscriber=profile, target_user=user)
    if all_subscriber.exists():
        return Response({True})
    return Response({False})


# узнать есть ли конкретный пользователь с profile_id у юзера
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def is_target_user(request, target_user_id_profile):
    profile = Profile.objects.get(id=target_user_id_profile)
    user = User.objects.get(id=request.user.id).user_profile
    # юзер в подписках у пользователя с profile_id
    all_target = Subscription.objects.filter(subscriber=user, target_user=profile)
    if all_target.exists():
        return Response({True})
    return Response({False})

