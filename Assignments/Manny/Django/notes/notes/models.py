from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    text = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')


# Create your models here.
