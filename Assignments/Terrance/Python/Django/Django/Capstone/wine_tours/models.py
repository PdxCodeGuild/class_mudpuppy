from django.db import models
from django.contrib.auth.models import User

class Vineyard(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=250)
    description = models.TextField()
    homepage = models.CharField(max_length=250)

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    party_size = models.IntegerField()
    vineyard = models.ForeignKey(Vineyard, on_delete=models.CASCADE)

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

