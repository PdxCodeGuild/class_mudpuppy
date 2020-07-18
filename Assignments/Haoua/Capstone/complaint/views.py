from django.shortcuts import render
from .models import Complaint
from django.views.generic import ListView, DetailView
# Create your views here.
# listview = allows us to see all blog psts
# detail = allows us to view a single blog post
# def complaint(request):
#     return render(request, 'complaint.html', {'complaints': Complaint.objects.all()})

class ComplaintView(ListView):
    model = Complaint
    template = 'complaint.html'

   