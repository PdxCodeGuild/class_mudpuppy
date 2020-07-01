from django.db import models

# Create your models here.
class TodoItem(models.Model):
    description_text = models.CharField(max_length=200, unique=True)
    created_date = models.DateField(auto_now_add=True)
    completed_date = models.DateField(blank=True, null=True)
    completed = models.BooleanField(default=False)