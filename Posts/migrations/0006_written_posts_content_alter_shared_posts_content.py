# Generated by Django 5.0.6 on 2024-06-04 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0005_remove_written_posts_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='written_posts',
            name='content',
            field=models.TextField(default=1, max_length=1500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shared_posts',
            name='content',
            field=models.TextField(blank=True, max_length=1500),
        ),
    ]
