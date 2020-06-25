from django.db import models

# Create your models here.
class Shorturl(models.Model):
    short = models.URLField(unique=True)
    longUrl = models.URLField(unique=True)
    

