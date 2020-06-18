from django.db import models

# Create your models here. This is where I start building the database, it's the first thing to do.
class ToDoItems(models.Model):
    todo_text = models.CharField(max_length=150)
    create_date = models.DateField('date started', auto_now=True)
    complete_date = models.DateField('date completed', blank=True, null=True)
    completed_bool = models.BooleanField(default=False)

    def __str__(self):
        return self
    