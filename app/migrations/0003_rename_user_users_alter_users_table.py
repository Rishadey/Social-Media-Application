# Generated by Django 5.0.6 on 2024-07-04 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_user_gender'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user',
            new_name='users',
        ),
        migrations.AlterModelTable(
            name='users',
            table='users',
        ),
    ]
