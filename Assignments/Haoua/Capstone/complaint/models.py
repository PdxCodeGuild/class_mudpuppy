from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Complaint(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    business = models.CharField(max_length=300)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=400)
    review = models.TextField()
    date = models.DateTimeField(default=timezone.now())


    def __str__(self):
        return str(self.business) + ' | ' + str(self.title) + ' | ' +str(self.name)

