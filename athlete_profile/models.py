import uuid

from django.db import models

from account.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    CHOICES_SPORTS = (
        ('ski', 'Лыжи'),
        ('run', 'Бег')
    )
    CHOICES_GENDER = (
        ('male', 'Мужчина'),
        ('female', 'Женщина')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=20, default='Аноним')
    surname = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=CHOICES_GENDER)
    sport_type = models.CharField(max_length=10, choices=CHOICES_SPORTS)
    characteristics = models.TextField()
    inventory = models.TextField()
    athlete_photo = models.ImageField(upload_to='athlete_photos/%Y/%m/%d', blank=True, null=True)
    inventory_photo = models.ImageField(upload_to='inventory_photos/%Y/%m/%d', blank=True, null=True)
    date_of_birth = models.DateField(null=True)
    city = models.CharField(max_length=50, null=True)
    contacts_messenger = models.TextField(null=True)

    def __str__(self):
        return f'{self.name} {self.surname}'


@receiver(post_save, sender=User)
def create_user_cart(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)