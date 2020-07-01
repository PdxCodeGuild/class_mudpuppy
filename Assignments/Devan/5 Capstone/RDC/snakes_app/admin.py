from django.contrib import admin
from .models import Snake

# Register your models here.


class SnakeAdmin(admin.ModelAdmin):
    pass




admin.site.register(Snake, SnakeAdmin)