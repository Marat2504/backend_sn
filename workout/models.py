from django.db import models

from athlete_profile.models import Profile


class Workout(models.Model):
    user = models.ForeignKey(Profile, related_name='user_workout', on_delete=models.CASCADE)
    distance = models.CharField(max_length=20)
    pace = models.CharField(max_length=20)
    duration = models.CharField(max_length=20)
    photo = models.ImageField(upload_to=f'workout_{user.name}/%Y/%m/%d', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user}: {self.distance}, {self.pace}, {self.distance}'

