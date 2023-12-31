import pytesseract
import os
import re

from django.conf import settings

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response


from .models import Workout
from athlete_profile.models import Profile

from PIL import Image

from .serializers import WorkoutSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_track(request, user_profile_uuid):
    profile = Profile.objects.get(id=user_profile_uuid)

    if 'file' in request.FILES:
        image = request.FILES['file']
        image_path = os.path.join(settings.MEDIA_ROOT, image.name)
        with open(image_path, 'wb') as file:
            for chunk in image.chunks():
                file.write(chunk)

        pytesseract.pytesseract.tesseract_cmd = settings.TESSERACT_CMD

        text = pytesseract.image_to_string(Image.open(image_path))

        os.remove(image_path)

        print('Здесь написано', text)

        # Найти значение длины дистанции
        distance = re.search(r'(\d+,\d+)\s', text)
        if distance:
            distance_value = distance.group(1)
        else:
            distance_value = '0'

        # Найти значение темпа
        paces = re.findall(r'(\d+:\d+)\s/', text)
        if paces:
            pace_value = paces[-1]
        else:
            pace_value = '0'

        # Найти значение времени дистанции
        times = re.findall(r'(\d+:\d+(?::\d+)*)\s', text)
        if times:
            if times[-1] == pace_value:
                time_value = times[-2]
            else:
                time_value = times[-1]
        else:
            time_value = '0'

        # Вывести найденные значения
        print("Расстояние '7,22 KM':", distance_value)
        print("Темп '4:50 /KM':", pace_value)
        print("Время '34:52':", time_value)

        workout = Workout.objects.create(user=profile, distance=distance_value,
                                         pace=pace_value, duration=time_value,
                                         photo=image)
        workout.save()

        serializer = WorkoutSerializer(workout)

        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_all_tracks(request, user_profile_uuid):
    print(request)
    profile = Profile.objects.get(id=user_profile_uuid)
    workouts = Workout.objects.filter(user=profile)

    serializer = WorkoutSerializer(workouts, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_track(request, track_id):
    track_response = request.data

    profile = request.user.user_profile
    track = Workout.objects.get(user=profile, id=track_id)

    if re.match(r'\d+:\d+(?::\d+)*', track_response['duration']) \
            and re.match(r'\d+,\d+', track_response['distance']) \
            and re.match(r'\d+:\d+', track_response['pace']):

        track.duration = track_response['duration']
        track.distance = track_response['distance']
        track.pace = track_response['pace']
        track.save()

        serializer = WorkoutSerializer(track)
        return Response(serializer.data)

    return Response('Ошибка при вводе данных')


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def del_track(request, track_id):
    profile = request.user.user_profile
    print(track_id)
    track = Workout.objects.get(user=profile, id=track_id)
    if track:
        serializer = WorkoutSerializer(track)
        track.delete()
        return Response(serializer.data)

    return Response({'Ошибка удаления'})
