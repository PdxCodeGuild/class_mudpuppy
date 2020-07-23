import random
import string
from django.conf import settings
SHORTURL_MIN = getattr(settings, "SHORTURL_MIN",8)

def create(chars=string.digits + string.ascii_lowercase + string.punctuation, size=SHORTURL_MIN):

    return ''.join(random.choice(chars) for _ in range(size))

def createshort(instance, size=SHORTURL_MIN):
    shortcode = create(size=size)
    Short = instance.__class__
    queryset = Short.objects.filter(shorturl =shortcode).exists()

    if queryset:
        return createshort(size=size)
    return shortcode