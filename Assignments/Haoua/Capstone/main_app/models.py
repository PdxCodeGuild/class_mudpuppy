from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # on_delete = if user deletes account, posts are deleted too
    title = models.CharField(max_length=140)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now())

    # engagement and reactions
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    fist = models.IntegerField()
    haha = models.IntegerField()
    angry = models.IntegerField()
    




# Create your models here.
