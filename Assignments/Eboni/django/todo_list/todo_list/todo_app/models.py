import datetime

from django.db import models

class TodoItem(models.Model):
    item_text = models.CharField(max_length=200)
    created_date = models.DateTimeField('date created', auto_now_add = True)
    complete_date = models.DateTimeField('date completed', null= True, blank= True) 
    item_complete = models.BooleanField(default=False)
    


# class Input(models.Model):
#     text = models.TextField()

    def __str__(self):
        return self.item_text


    

# Create your models here.
