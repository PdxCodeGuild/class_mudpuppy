from django.contrib import admin
from .models import Link, Comment

# Register your models here.


class LinkAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Link, LinkAdmin)
admin.site.register(Comment, CommentAdmin)
