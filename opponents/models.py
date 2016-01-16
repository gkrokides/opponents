from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Sport (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Player (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    whole_name = models.CharField(max_length=100, blank=True, null=True)
    sports = models.ManyToManyField(Sport)

    def save(self, *args, **kwargs):
        self.whole_name = self.first_name+" "+self.last_name
        super(Player, self).save(*args, **kwargs)

    def __str__(self):
        return self.whole_name


class Rating(models.Model):
    RATINGS = [(i,i) for i in range(5)]
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    self_rating = models.IntegerField(choices=RATINGS)
    opponents_rating =  models.IntegerField(choices=RATINGS)