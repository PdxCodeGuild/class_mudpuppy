from django.contrib import admin
from .models import BallPython


class BallPythonAdmin(admin.ModelAdmin):
    pass


admin.site.register(BallPython, BallPythonAdmin)