# Generated by Django 4.2.7 on 2023-12-30 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('athlete_profile', '0006_alter_profile_gender_alter_profile_sport_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.FloatField()),
                ('pace', models.FloatField()),
                ('duration', models.DurationField()),
                ('photo', models.ImageField(blank=True, upload_to='workout_None/%Y/%m/%d')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_workout', to='athlete_profile.profile')),
            ],
        ),
    ]
