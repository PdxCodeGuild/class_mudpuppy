from django.db import models

class URL(models.Model):
    short = models.CharField(max_length=8, unique=True)
    full = models.CharField(max_length=240, unique=False)

# Create your models here.
