from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Code
from django.utils.crypto import get_random_string

# Create your views here.

def index(request):
    urls = Code.objects.all()
    print('ok')
    context = {'urls': urls}
    return render(request, 'shortener_app/index.html', context)

def shorten(request):
    print(request.body)
    print(request.POST)
    print(request.POST["new"])
    new_code = Code(first_code=request.POST["new"], second_code=get_random_string(length=6))
    new_code.save()
    return HttpResponseRedirect(reverse('shortener:index'))

def redirection(request, second_code):
    new_code = Code.objects.get(second_code=second_code)
    return redirect(new_code.first_code)




