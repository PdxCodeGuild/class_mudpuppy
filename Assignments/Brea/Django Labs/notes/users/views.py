# users views.py
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.contrib.auth import login as _login, logout as _logout, authenticate as auth
from django.contrib.auth.models import User


# Create your views here.

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth(request, username=username, password=password)
    _login(request, user)
    return HttpResponseRedirect(reverse('notes:index'))

def logout(request):    #if I link to this, then the user will be logged out
    _logout(request)
    return HttpResponseRedirect(reverse('users:rl_page'))

def register(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    new_user = User.objects.create_user(username, email, password)
    _login(request, new_user)
    return HttpResponseRedirect(reverse('notes:index'))
    #at the top: from django.contrib.auth.models import User

def rl_page(request):
    next_place = request.GET.get('next', reverse('notes:index'))
    context = {
        'next': next_place,
    }
    return render(request, 'users/template.html', context)


