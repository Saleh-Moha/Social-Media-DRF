# Generated by Django 5.0.6 on 2024-06-22 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0008_remove_follow_request_accept_follow_request_status'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='follow_request',
            unique_together={('requester', 'requested')},
        ),
    ]
