from django.core.files.storage import FileSystemStorage
from django.db import models
import os
from django.conf import settings


class Genetic(models.Model):
    gene = models.CharField(max_length=128)

    def __str__(self):
        return self.gene


class BallPython(models.Model):
    gender_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    feeder_CHOICES = [
        ('LFR', 'Live Fuzzy Rat'),
        ('LPR', 'Live Pup Rat'),
        ('LWR', 'Live Weanling Rat'),
        ('LSR', 'Live Small Rat'),
        ('FSM', 'F/T Fuzzy Rat'),
        ('FWR', 'F/T Weanling Rat'),
        ('FPR', 'F/T Pup Rat'),
        ('FSR', 'F/T Small Rat'),
    ]
    morph = models.ManyToManyField(Genetic, related_name="ballpythons")
    name = models.CharField(max_length=128)
    gender = models.CharField(max_length=1, choices=gender_CHOICES)
    weight = models.FloatField(default=100)
    weighed_on = models.DateField()
    feeding_on = models.CharField(
        max_length=3, choices=feeder_CHOICES, default='LFR')
    hatched_on = models.DateField()
    cost_in_dollars = models.FloatField()
    picture = models.ImageField(upload_to=os.path.join('ball_pythons', 'img'))
    listed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
