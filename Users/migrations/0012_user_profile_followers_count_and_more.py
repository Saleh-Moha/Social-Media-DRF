# Generated by Django 5.0.6 on 2024-06-27 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0011_remove_user_profile_followers_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='followers_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='followings_count',
            field=models.IntegerField(default=0),
        ),
    ]
