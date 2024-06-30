# Generated by Django 5.0.6 on 2024-06-27 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0009_alter_follow_request_unique_together'),
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
