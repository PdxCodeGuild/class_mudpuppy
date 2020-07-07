from django.shortcuts import render, reverse, redirect
# from django.http import HttpResponse

#creating a function called home that takes in a request argument
#return what we want the user to see when we take them to this rout

# Create your views here.
posts = [
    {
        'author': 'louis onla',
        'content': 'get rich or die trying',
        'title': 'blog title',
        'date_posted': 'august 8, 2020',
    
    
    
    
    }

    {
        'author': 'mary jane',
        'content': 'get richer or die tryinger',
        'title': 'blog title 2'
        'date_posted': 'august 10, 2020',
    
    
    
    
    }





]
def home(request):
    # list of dictionaries with each blog post
    context = {
        'posts': posts
    }


    #return a string that tells us we are at the blog home
    return render(request, 'blog_app/home.html', context)
    # passes data into templaate to make it accessible


def about(request):
    
    #return a string that tells us we are at the blog home
    return render(request, 'blog_app/about.html', {'title':title})