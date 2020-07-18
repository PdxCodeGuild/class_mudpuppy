from django.shortcuts import render
from .models import Complaint
# Create your views here.
def complaint(request):
    return render(request, 'complaint.html', {'complaints': Complaint.objects.all()})
