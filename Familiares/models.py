from django.db import models

# Create your models here.


class Familiar(models.Model):

    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.IntegerField()
    relation = models.CharField(max_length=20)
    birthday = models.DateTimeField()
