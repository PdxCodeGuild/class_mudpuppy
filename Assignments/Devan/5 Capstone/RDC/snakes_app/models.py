from django.db import models

# Create your models here.


class Snake(models.Model):
    name = models.CharField(max_length=128)
    gender_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    gender = models.CharField(max_length=1, choices=gender_CHOICES)
    hatched_on = models.DateTimeField()
    cost_in_dollars = models.FloatField()
    picture = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.name
