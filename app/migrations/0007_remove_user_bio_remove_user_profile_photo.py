# Generated by Django 5.0.6 on 2024-07-09 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_user_bio_user_profile_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='user',
            name='profile_photo',
        ),
    ]
