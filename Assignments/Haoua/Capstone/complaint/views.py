
from .models import Complaint, PersonComplaint
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required

# Create your views here.
# listview = allows us to see all blog psts
# detail = allows us to view a single blog post
# def complaint(request):
#     return render(request, 'complaint.html', {'complaints': Complaint.objects.all()})

class ComplaintView(ListView):
    model = Complaint
    template_name = 'complaint_list.html'
    def __unicode__(self):
        return self.template_name


class ComplaintDetailView(DetailView):
    model = Complaint
    template_name = 'complaint_detail.html'
   
    def __unicode__(self):
        return self.template_name


class CreateComplaint(CreateView):
    model = Complaint
    template_name = 'complaint_form.html'
    fields = "__all__"

    def __unicode__(self):
        return self.template_name

    

    # def create(request):
    #     return render(request, 'complaint/complaint_form.html')

class PersonCreateComplaint(CreateView):
    model = PersonComplaint
    template_name = 'personcomplaint_form.html'
    fields = "__all__"
  
    def __unicode__(self):
        return self.template_name

    

class PersonView(ListView):
    model = PersonComplaint
    template_name = 'personcomplaint_list.html'

    def __unicode__(self):
        return self.template_name


class PersonDetailView(DetailView):
    model = PersonComplaint
    template_name = 'personcomplaint_detail.html'

    
    def get_queryset(self):
        variable = PersonComplaint.objects.filter(date__lte=timezone.now())
        print(variable)
        return variable
        
    def __unicode__(self):
        return self.template_name
    
