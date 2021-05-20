# Generated by Django 3.2.3 on 2021-05-19 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweetcore', '0004_followers_date_db_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twusers',
            name='name',
            field=models.CharField(default='-999', max_length=50),
        ),
        migrations.AlterField(
            model_name='twusers',
            name='tw_account_created_at',
            field=models.DateTimeField(default='1999-01-01', verbose_name='date user created'),
        ),
        migrations.AlterField(
            model_name='twusers',
            name='tw_screen',
            field=models.CharField(default='-999', max_length=50),
        ),
        migrations.CreateModel(
            name='MetaFollowers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_follower', models.CharField(max_length=200)),
                ('following_position', models.IntegerField()),
                ('is_all_history_done', models.BooleanField(default=False, verbose_name='Are all followers exported')),
                ('tw_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweetcore.twusers')),
            ],
        ),
    ]
