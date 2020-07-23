from django.db import models
from django.conf import settings
from .utils import create
from django.urls import reverse


SHORTURL_MAX = getattr(settings, "SHORTURL_MAX",8)


# # Create your models here.(si)

# class ShortUrlManager(models.Manager):
#     def all(self, *args, **kwargs):
#         queryset = super(ShortUrlManager, self).all(*args, **kwargs )
#         qs = queryset.filter(active=True)
#         return qs


# class Shorturl(models.Model):
#     # short = models.URLField(unique=True)
#     # longUrl = models.URLField(unique=True)
#     longurl = models.CharField(max_length=200,)
#     shorturl = models.CharField(max_length=SHORTURL_MAX,unique=True, blank="true")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  

#     def save(self, *args, **kwargs):
#         if self.shorturl is None or self.shorturl =="":

#             self.shorturl = createshort(self)
#         super(Shorturl, self).save(*args, **kwargs)

#     def __str__(self):
#         return str(self.longurl) + str(self.shorturl) + '|' + str(self.id)
#     def __unicode__(self):
#         return str(self.longurl) +str(self.shorturl) + '|'+ str(self.id)
    
#     def get_absolute_url(self):
#         return reverse('shorturl')
class Shorturl(models.Model):
    longurl = models.CharField(max_length=200)
    shorturl = models.CharField(max_length=8, unique=True)

    def __str__(self):
        web = self.longurl.split('.')
        return web[1]