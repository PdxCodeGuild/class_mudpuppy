from django.shortcuts import render
from django.http import HttpResponse

#creating a function called home that takes in a request argument
#return what we want the user to see when we take them to this rout

# Create your views here.

def home(request):
    #return a string that tells us we are at the blog home
    return HttpResponse('<h1>Blog Home</h1>')

def about(request):
    #return a string that tells us we are at the blog home
    return HttpResponse('<h1>Blog Aboute</h1>')