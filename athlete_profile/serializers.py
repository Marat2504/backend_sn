from rest_framework import serializers
from .models import Profile, ProfilePhoto


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfilePhotoSerializer(serializers.ModelSerializer):
    # profile = ProfileSerializer(read_only=True)

    class Meta:
        model = ProfilePhoto
        fields = ['id', 'photo', 'upload_date']