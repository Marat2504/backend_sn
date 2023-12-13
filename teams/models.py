import uuid

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.utils.text import slugify
from autoslug import AutoSlugField

from account.models import User


class Team(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = AutoSlugField(populate_from='name', unique=True)
    avatar = models.ImageField(upload_to='teams_avatars/%Y/%m/%d',
                               default='teams_avatars/avatarTeams.png',
                               blank=True, null=True)
    captain_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='captain_teams')
    count_members = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='members')

    def __str__(self):
        return f'{self.team.name}: {self.user.username}'


@receiver(post_save, sender=Team)
def create_teammember(sender, instance, created, **kwargs):
    if created:
        TeamMember.objects.create(team=instance, user=instance.captain_id)


