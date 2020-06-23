from django.db import models
import string

chars_nums = string.ascii_letters+string.digits


class URL(models.Model):
    full_url = models.URLField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    clicks = models.IntegerField(default=0)
