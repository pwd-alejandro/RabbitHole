# Generated by Django 3.2.3 on 2021-05-19 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweetcore', '0003_remove_twusers_follower'),
    ]

    operations = [
        migrations.AddField(
            model_name='followers',
            name='date_db_added',
            field=models.DateTimeField(default='1999-01-01', verbose_name='date follower was created in db'),
        ),
    ]
