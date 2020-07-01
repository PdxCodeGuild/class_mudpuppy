from django.db import models

class Sign(models.Model):
    sign = models.CharField(max_length= 20)

class Birthday(models.Model):
    date = models.DateField(null=True, blank=True)
    sign = models.ForeignKey(Sign, null=True, on_delete=models.PROTECT)

    


# Create your models here.
