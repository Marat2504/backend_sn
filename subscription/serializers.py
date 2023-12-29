from rest_framework import serializers

from athlete_profile.serializers import ProfileSerializer
from .models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        subscriber = ProfileSerializer(read_only=True)
        target_user = ProfileSerializer(read_only=True)
        model = Subscription
        fields = ['id', 'subscriber', 'target_user']

        depth = 1

