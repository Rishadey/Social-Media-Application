# Generated by Django 5.0.6 on 2024-07-04 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_user_users_alter_users_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='users',
            new_name='user',
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]
