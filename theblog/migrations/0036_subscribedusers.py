# Generated by Django 4.0.5 on 2022-07-31 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0035_remove_profile_email_confirmed'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscribedUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]