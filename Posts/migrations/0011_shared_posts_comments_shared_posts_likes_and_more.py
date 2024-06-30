# Generated by Django 5.0.6 on 2024-06-27 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0010_shared_posts_is_private_written_posts_is_private'),
    ]

    operations = [
        migrations.AddField(
            model_name='shared_posts',
            name='comments',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='shared_posts',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='shared_posts',
            name='shares',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='written_posts',
            name='comments',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='written_posts',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='written_posts',
            name='shares',
            field=models.IntegerField(default=0),
        ),
    ]
