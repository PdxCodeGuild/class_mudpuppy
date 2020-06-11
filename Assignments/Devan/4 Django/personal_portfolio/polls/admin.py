from django.contrib import admin

from .models import Question, Choice


class PollsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Question)
admin.site.register(Choice)
