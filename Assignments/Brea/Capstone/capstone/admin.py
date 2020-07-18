from django.contrib import admin

# Register your models here.
from .models import Song, Genre, Review

admin.site.register(Song)
admin.site.register(Genre)
admin.site.register(Review)