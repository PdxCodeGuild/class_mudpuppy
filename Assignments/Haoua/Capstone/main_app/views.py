from django.shortcuts import render
from django.utils import timezone
from .models import Post
# Create youmr views here.
def home(request):

    return render(request,'main_app/landing.html', {'posts': Post.objects.all()})

def about(request):
    return render(request,'main_app/about.html')
    

def blog(request):
    return render(request, 'main_app/blog.html',{'posts': Post.objects.all()})

def index(request):
    
    return(Post.date)