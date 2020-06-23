from django.contrib import admin
from .models import URL

# Register your models here.


class UrlAdmin(admin.ModelAdmin):
    pass


admin.site.register(URL, UrlAdmin)
