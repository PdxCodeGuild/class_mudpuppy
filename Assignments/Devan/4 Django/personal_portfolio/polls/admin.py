from django.contrib import admin

from .models import Question


class PollsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Question)
