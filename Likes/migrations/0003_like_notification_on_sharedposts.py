# Generated by Django 5.0.6 on 2024-06-28 22:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Likes', '0002_like_notification_on_writtenposts'),
        ('Posts', '0016_remove_video_post_written_posts_image_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Like_Notification_on_SharedPosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('liked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='whohasbeenlikeshared', to=settings.AUTH_USER_MODEL)),
                ('liker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wholikesshared', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Posts.written_posts')),
            ],
        ),
    ]