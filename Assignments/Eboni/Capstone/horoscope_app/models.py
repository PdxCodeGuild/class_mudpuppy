from django.db import models

class Birthday(models.Model):
    char = models.CharField(max_length=6)

    def __str__(self):
        return self.char

# Create your models here.
