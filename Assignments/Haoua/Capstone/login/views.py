from django.shortcuts import render, redirect, reverse
from django.contrib import messages
# Create your views here. 

from .forms import Register 
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f"Welcome {username}, you've created an account.")
            return redirect('signin/')
            # if I have time homepage will only be accessible to users and a landing page accessible to everyone

    
    else:
        form = Register(request.POST)
        # messages.error(request, f"Please try again")


    return render(request, 'login/signup.html', {'form':form})

@login_required

def account(request):
    return render(request, 'login/account.html')