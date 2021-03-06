from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

def rl_page(request):
    data = request.GET
    context = {
        'next' : data.get('next', '/notes/')
    }
    return render(
        request,
        'user/register_login.html',
        context
        )
def register(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    new_user = User.objects.create_user(username, email, password)
    login(request, new_user)
    return HttpResponseRedirect('/notes/')
    
def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    login(request, user)
    return HttpResponseRedirect(request.POST['next'])
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:rl_page'))       