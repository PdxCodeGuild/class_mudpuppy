from django.db import models
from links_app.models import Link, Comment # Changed line
from django.utils.text import slugify

class Link(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, unique=True)
    link = models.CharField(max_length=128)

    def __str__(self):
        return self.slug[:10]

    def __repr__(self):
        return self.slug[:10]

class Comment(models.Model):
    Link.objects.get_or_create(
                                       name=pairing[0],
                                       slug=slugify(pairing[0]),
                                       link=pairing[1]
                               )

    google_link = Link.objects.get(link="google.com") # New line
    for text in ('I love this site!', 'I hate this site!'): # New line
        Comment.objects.get_or_create( # New line
            text=text, # New line
            link_id=google_link.id, # New line
                                       ) # New line


