from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse

#creating a function called home that takes in a request argument
#return what we want the user to see when we take them to this rout

# Create your views here.
posts = [
    {
        'author': 'louis onla',
        'content': 'get rich or die trying',
        'title': 'blog title',
        'date': 'august 8, 2020',
    }
]
def home(request):
    context = {
        'posts': posts
    }
    #return a string that tells us we are at the blog home
    return render(request, 'blog_app/home.html', context)

def about(request):
    
    #return a string that tells us we are at the blog home
    return render(request, 'blog_app/about.html')