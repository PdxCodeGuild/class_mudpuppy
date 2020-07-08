from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required 


def rl_page (request):
    return render(request, "user/register_login.html")

def register(request):
    pass
def login_view(request):
    pass
def logout_view(request):
    pass    
