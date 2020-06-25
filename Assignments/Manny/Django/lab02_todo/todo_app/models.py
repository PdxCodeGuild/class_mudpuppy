from django.db import models


class ToDo(models.Model):
    task = models.CharField(max_length=32)
    created = models.DateTimeField(auto_now_add=True) #auto now add for created
    mod = models.DateTimeField(auto_now=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.task

# class DateTimeField(auto_now=False, auto_now_add=False, **options) 
# class BooleanField(**options)
# class CharField(max_length=None, **options)