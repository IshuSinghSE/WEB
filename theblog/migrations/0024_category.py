# Generated by Django 4.0.5 on 2022-07-29 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0023_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]