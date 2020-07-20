from django.contrib import admin

from . models import Complaint, PersonComplaint

admin.site.register(Complaint)
admin.site.register(PersonComplaint)

