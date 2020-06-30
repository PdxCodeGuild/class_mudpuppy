from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
# Create your views here.
from django.contrib.auth import login as _login, logout as _logout, authenticate as auth

def login(request):
    username = request.POST['username']
    password = request.POST['password']

    user = auth(request, username=username, password=password)
    _login(request, user)
    # below tells the browser to go to a new place
    # it looks inside note directory
    # httpresponse redirect redirect to another page, we can add a direct link inside parenthesis
    # return HttpResponseRedirect(reverse('notes:index'))
    return HttpResponseRedirect(request.POST['next'])
def logout(request):
    _logout(request)
    # use reverse to get there using a nickname
    return HttpResponseRedirect(reverse('users:rl_page'))

def register(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    new_user = User.objects.create_user(username, email, password)
    _login(request, new_user)
    return HttpResponseRedirect(reverse('notes:index'))

def rl_page(request):
    next_place = request.GET.get('next', reverse('notes:index'))
    context = {
        'next': next_place,

    }
    return render(request, 'users/register.html', context)