import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)




# # Таблица "Teams"
# class Team(models.Model):
#     team_id = models.AutoField(primary_key=True)
#     team_name = models.CharField(max_length=255)
#     captain_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     description = models.TextField()
#
# # Таблица "Team_Members"
# class TeamMember(models.Model):
#     team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#
# # Таблица "Trainings"
# class Training(models.Model):
#     training_id = models.AutoField(primary_key=True)
#     training_name = models.CharField(max_length=255)
#     team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
#     location = models.CharField(max_length=255)
#     date_time = models.DateTimeField()
#
# # Таблица "Events"
# class Event(models.Model):
#     event_id = models.AutoField(primary_key=True)
#     event_name = models.CharField(max_length=255)
#     team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
#     location = models.CharField(max_length=255)
#     date_time = models.DateTimeField()
#     entry_fee = models.DecimalField(max_digits=8, decimal_places=2)
#     target_entries = models.PositiveIntegerField()
#
#
# # Таблица "Coaches"
# class Coach(models.Model):
#     coach_id = models.AutoField(primary_key=True)
#     coach_name = models.CharField(max_length=255)
#     sport_type = models.CharField(max_length=255)
#     price = models.DecimalField(max_digits=8, decimal_places=2)
#
# # Таблица "Sport_Types"
# class SportType(models.Model):
#     sport_type = models.CharField(primary_key=True, max_length=255)




