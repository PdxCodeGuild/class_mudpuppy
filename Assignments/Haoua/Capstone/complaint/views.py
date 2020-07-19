from django.shortcuts import render
from .models import Complaint
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required

# Create your views here.
# listview = allows us to see all blog psts
# detail = allows us to view a single blog post
# def complaint(request):
#     return render(request, 'complaint.html', {'complaints': Complaint.objects.all()})

class ComplaintView(ListView):
    model = Complaint
    template= 'complaint_list.html'


class ComplaintDetail(DetailView):
    model = Complaint
    template = 'complaint_detail.html'
   



class CreateComplaint(CreateView):
    fields = ('title','business','phone', 'email','address', 'review', 'date')
    model = Complaint
    template = 'complaint_form.html'
    # fields = ('title','business','phone', 'email','address', 'review', 'date')

