from django.db import models
from athlete_profile.models import Profile


class Subscription(models.Model):
    subscriber = models.ForeignKey(Profile, related_name='subscriptions', on_delete=models.CASCADE)
    target_user = models.ForeignKey(Profile, related_name='subscribers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('subscriber', 'target_user')

    def __str__(self):
        return f'{self.subscriber} подписан на {self.target_user}'