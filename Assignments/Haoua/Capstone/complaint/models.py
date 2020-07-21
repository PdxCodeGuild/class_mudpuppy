from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Complaint(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE,default='2', null=True)
    title = models.CharField(max_length=200)
    business = models.CharField(max_length=300)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=400)
    review = models.TextField()
    date = models.DateTimeField(default=timezone.now())
    email = models.EmailField()

    def __str__(self):
        return str(self.business) + ' | ' + str(self.title) + ' | ' + str(self.name) 

    def get_absolute_url(self):
        return reverse('complaints', args=(str(self.id)))


class PersonComplaint(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE,default='2', null=True)
    title = models.CharField(max_length=200)
    perpetrator = models.CharField(max_length=300)
    job_phone = models.CharField(max_length=200)
    job_email = models.EmailField()
    job = models.CharField(max_length=300)
    social_media = models.CharField(max_length=400)
    review = models.TextField()
    date = models.DateTimeField(default=timezone.now())



    def __str__(self):
        return str(self.perpetrator) + ' | ' + str(self.title) + ' | ' + str(User.user.username) 

    def get_absolute_url(self):
        return reverse('persons', args=(str(self.id)))