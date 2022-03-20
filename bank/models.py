from operator import mod
from django.db import models

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    balance = models.IntegerField(max_length=1000)

    def __str__(self):
        return self.name