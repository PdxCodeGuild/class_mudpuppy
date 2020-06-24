from django.db import models

# Create your models here.

class Urls(models.Model):
    org_url = models.CharField(max_length=200)
    short_url = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return f'website: {self.org_url.rstrip("https://").rstrip("http://").rstrip("www.")[:10]}' #look up if I can combine multiple rstrip within a single parentheses with ,
    