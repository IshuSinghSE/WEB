# Generated by Django 4.0.5 on 2022-07-24 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0009_alter_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(blank=True, default='coding', max_length=200, null=True),
        ),
    ]
