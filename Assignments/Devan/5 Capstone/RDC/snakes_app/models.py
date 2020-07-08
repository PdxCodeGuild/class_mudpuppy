from django.core.files.storage import FileSystemStorage
from django.db import models

fs = FileSystemStorage(location='snakes_app/media/photos')


class Snake(models.Model):
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

    name = models.CharField(max_length=128)
    gender = models.CharField(max_length=1, choices=gender_CHOICES)
    weight = models.FloatField(default=100)
    weighed_on = models.DateField()
    feeding_on = models.CharField(max_length=3, choices=feeder_CHOICES, default='LFR')
    hatched_on = models.DateField()
    cost_in_dollars = models.FloatField()
    picture = models.ImageField(storage=fs)

    def __str__(self):
        return self.name
