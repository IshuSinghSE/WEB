# Generated by Django 4.0.5 on 2022-07-31 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0034_profile_email_confirmed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email_confirmed',
        ),
    ]
