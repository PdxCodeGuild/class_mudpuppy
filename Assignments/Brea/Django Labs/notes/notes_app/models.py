# notes_app/models.py
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    text = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')  #typing user.notes would give us all the notes associated with a user's unique id
