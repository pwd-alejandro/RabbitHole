from django.db import models


class TwUsers(models.Model):
    tw_id = models.CharField(max_length=200)
    tw_screen = models.CharField(max_length=50, default='-999')
    name = models.CharField(max_length=50, default='-999')
    tw_account_created_at = models.DateTimeField('date user created', default='1999-01-01')
    protected = models.BooleanField('Is account protected or private', default=False)
    verified = models.BooleanField('Is account verified', default=False)


class Followers(models.Model):
    tw_id = models.CharField(max_length=200, default='-111')
    following_tw_id = models.CharField(max_length=200)
    following_position = models.IntegerField()
    date_db_added = models.DateTimeField('date follower was created in db', default='1999-01-01')

