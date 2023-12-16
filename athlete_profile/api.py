from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from account.models import User
from teams.models import Team
from .models import Profile
from .serializers import ProfileSerializer, ProfilePhotoSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_profile(request, user_profile_uuid):
    try:
        profile = Profile.objects.get(id=user_profile_uuid)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ProfileSerializer(profile)
    return Response(serializer.data)


@api_view(['PUT'])
def edit_profile(request, uuid_profile):
    try:
        profile = Profile.objects.get(id=uuid_profile)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ProfileSerializer(profile, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_photo(request, uuid_profile):
    try:
        profile = Profile.objects.get(id=uuid_profile)
        photos = profile.inventory_photos.all().order_by('-upload_date')
        print(photos)
        serializer = ProfilePhotoSerializer(photos, many=True)
        return Response(serializer.data)

    except Profile.DoesNotExist:
        return Response({'error': 'Profile not found'})


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_captain_team(request, slug_team):
    try:
        team = Team.objects.get(slug=slug_team)
        captain_id = team.captain_id_id
        profile = Profile.objects.get(user_id=captain_id)

        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    except (Team.DoesNotExist, Profile.DoesNotExist, User.DoesNotExist):
        return Response({'error': 'Captain profile not found'}, status=status.HTTP_404_NOT_FOUND)




