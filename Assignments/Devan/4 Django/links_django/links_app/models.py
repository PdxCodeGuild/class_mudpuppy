from django.db import models

# Create your models here.


class Link(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, unique=True)
    link = models.CharField(max_length=128)

    def __str__(self):
        return self.slug

    def __repr__(self):
        return self.slug[:10]


class Comment(models.Model):
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.link.id, self.text
