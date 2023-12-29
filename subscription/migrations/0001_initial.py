# Generated by Django 4.2.7 on 2023-12-27 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('athlete_profile', '0006_alter_profile_gender_alter_profile_sport_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='athlete_profile.profile')),
                ('target_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscribers', to='athlete_profile.profile')),
            ],
            options={
                'unique_together': {('subscriber', 'target_user')},
            },
        ),
    ]
