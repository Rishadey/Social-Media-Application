# Generated by Django 5.0.6 on 2024-07-05 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_users_user_alter_user_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='picfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=50)),
                ('purl', models.ImageField(upload_to='')),
            ],
            options={
                'db_table': 'picfile',
            },
        ),
    ]