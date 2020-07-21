
from .models import Complaint, PersonComplaint
from .forms import ComplaintForm
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


class ComplaintDetailView(DetailView):
    model = Complaint
    template_name = 'complaint_detail.html'
   



class CreateComplaint(CreateView):
    model = Complaint
    template_name = 'complaint_form.html'
    fields = "__all__"



    

    # def create(request):
    #     return render(request, 'complaint/complaint_form.html')

class PersonCreateComplaint(CreateView):
    model = PersonComplaint
    form_class= ComplaintForm
    template_name = 'personcomplaint_form.html'
    # fields = ('title','business','phone', 'email','address', 'review', 'date')
    # fields = "__all__"
  
    # def dispatch(self, *args, **kwargs):
    #     return super(PersonCreateComplaint, self).dispatch(*args,**kwargs)
    # def form_valid(self,form):
    #     obj = form.save(commit=False)
    # #     obj.name = self.request.user
    # #     obj.save()
    # def get_initial(self):
    #     self.initial.update({'name': self.request.user})
    #     return self.initial
    

class PersonView(ListView):
    model = PersonComplaint
    template_name = 'personcomplaint_list.html'


class PersonDetailView(DetailView):
    model = PersonComplaint
    template_name = 'personcomplaint_detail.html'