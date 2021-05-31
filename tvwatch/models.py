from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Model
from django.utils import timezone

class User(AbstractUser):
    pass

class Tvshow(models.Model):
    user = models.ForeignKey('User', on_delete = models.CASCADE, null = True, related_name = 'tvshow')
    release_year=models.CharField(max_length=15)
    language=models.CharField(max_length=200)
    genre=models.CharField(max_length=250)
    vote_average=models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.user}"

class Mylist(models.Model):
    user = models.ForeignKey('User', on_delete = models.CASCADE, null = True, related_name = 'mylist')
    mylist = models.CharField(max_length=250)
    tvid = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.mylist}"

class Newsletter(models.Model):
    newsletter = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.newsletter}"