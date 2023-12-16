from django.contrib.auth.models import AnonymousUser

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from .forms import TeamForm
from account.models import User
from .models import Team, TeamMember
from .serializers import TeamSerializer, TeamCreateSerializer, TeamMemberSerializer

from athlete_profile.models import Profile
from athlete_profile.serializers import ProfileSerializer


# получить список команд
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_teams(request, user_id=None):
    teams = Team.objects.all()
    if user_id is not None:
        try:
            user = User.objects.get(id=user_id)
            serializer = TeamSerializer(teams, context={'user': user},
                                        many=True)
            return Response(serializer.data)

        except Team.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)


# вступить в команду
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def is_subscribe(request, team_id, user_id):
    try:
        team = Team.objects.get(id=team_id)
        user = User.objects.get(id=user_id)

        # Проверяем, есть ли пользователь уже в команде
        try:
            team_member = TeamMember.objects.get(team=team, user=user)
            team_member.delete()  # Если пользователь уже в команде, удаляем его
            team.count_members -= 1
            team.save()
            print(team.count_members)
            return Response({'message': 'клиент удален из команды'}, status=status.HTTP_200_OK)
        except TeamMember.DoesNotExist:
            team_member = TeamMember(team=team, user=user)
            team_member.save()  # Если пользователь не в команде, добавляем его
            team.count_members += 1
            team.save()
            print(team.count_members)
            return Response({'message': 'клиент вступил в команду'}, status=status.HTTP_201_CREATED)
    except (Team.DoesNotExist, User.DoesNotExist):
        return Response({'message': 'Team or User not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_team(request):
    user_id = request.user.id
    print(request.data)

    form_data = {
        'name': request.data.get('name'),
        'description': request.data.get('description'),
        'captain_id': user_id
    }
    try:
        form_data.update({'avatar': request.FILES['avatar']})
    except Exception:
        pass

    serializer = TeamCreateSerializer(data=form_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_current_team(request, slug_team):
    try:
        current_team = Team.objects.get(slug=slug_team)
        serializer = TeamSerializer(current_team, context={'user': request.user})
        return Response(serializer.data)
    except Team.DoesNotExist:
        return Response({'error': 'Team or User not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_current_team_athletes(request, slug_team):
    try:
        profiles = Profile.objects.filter(user__members__team__slug=slug_team)
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
    except Profile.DoesNotExist:
        return Response({'error': 'Current team profiles not found'}, status=status.HTTP_404_NOT_FOUND)






# @api_view(['GET'])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def get_teams(request, user_id=None):
#     if user_id is not None:
#         try:
#             user = User.objects.get(id=user_id)
#             teams = Team.objects.all()
#             if user != AnonymousUser():
#                 serializer = TeamSerializer(teams, context={'user': user},
#                                             many=True)
#                 return Response(serializer.data)
#             else:
#                 user = None
#                 serializer = TeamSerializer(teams, context={'user': user},
#                                             many=True)
#                 return Response(serializer.data)
#
#         except Team.DoesNotExist:
#             print('null')
#             return Response(status=status.HTTP_404_NOT_FOUND)