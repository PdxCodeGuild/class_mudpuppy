import datetime

from django.db import models

class TodoItem(models.Model):
    item_text = models.CharField(max_length=200)
    created_date = models.DateTimeField('date created', auto_now = True)
    complete_date = models.DateTimeField('date completed')

    def __str__(self):
        return self.item_text

class ItemComplete(models.Model):
    Incomplete = 'No'
    Complete = 'Yes'
    task_complete = [
        (Incomplete, 'No'),
        (Complete, 'Yes'),
    ]
    task_complete = models.CharField(max_length=50,
    choices=task_complete,)
    # def __str__(self):
    #     return self.start_date
    # def __str__(self):
    #     return self.complete_date

# Create your models here.
