# Generated by Django 5.0.6 on 2024-06-28 13:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0012_remove_shared_posts_shares'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='written_posts',
            name='image',
        ),
        migrations.RemoveField(
            model_name='written_posts',
            name='video',
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='Posts.written_posts')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='Posts.written_posts')),
            ],
        ),
    ]
