from django.contrib import admin

from . models import Complaint, PersonComplaint, Detail

admin.site.register(Complaint)
admin.site.register(PersonComplaint)


