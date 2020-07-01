from django.db import models


class URL(models.Model):
    full_url = models.URLField(unique=True)
    tiny_url = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    clicks = models.IntegerField(default=0)

    def __str__(self):
        website = self.full_url.split('.')
        return website[1]
