from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # on_delete = if user deletes account, posts are deleted too
    title = models.CharField(max_length=140)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now())



    def __str__(self):
        self.author
        self.title
        self.content
        self.date

        return self.title
    



# class Comments(models.Model):
    
    




# Create your models here.
