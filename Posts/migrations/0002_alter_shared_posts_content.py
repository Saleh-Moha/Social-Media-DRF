# Generated by Django 5.0.6 on 2024-06-04 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shared_posts',
            name='content',
            field=models.TextField(blank=True, max_length=1500),
        ),
    ]