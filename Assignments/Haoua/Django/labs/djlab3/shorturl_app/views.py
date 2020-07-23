from django.shortcuts import render, redirect,reverse
from django.http import HttpResponseRedirect, HttpResponse
from . models import Shorturl
from django.views.generic import CreateView, ListView
from django.template import loader
import string
import random

# Create your views here.
def index(request):
    context=None
    if request.method == "POST":
        final = Shorturl(longurl=request.POST['old'], shorturl=CreateUrl())
        final.save()
        context = {
            'data':final,
        }
    return render(request, 'shorturl_app/shorturls.html', context)

# def short(request, shorturl=None, *args, **kwargs):
#     # return redirect("shorturl_app.urls")
#     print(shorturl)
#     print(kwargs)
#     return HttpResponse("hi {su}")
def CreateUrl(i):
    words = string.ascii_letters + string.digits 
    shortcode = ""

    for i in range(8):
        code = random.choice(str(words))
        shortcode += code
    return shortcode

def redirect(request, param):
    redirect = Shorturl.objects.get(shorturl=param)

    return HttpResponseRedirect(f'https://{redirect.longurl}')
# class CreateShorturl(CreateView):
#     model = Shorturl
#     template_name = 'shorturl_form.html'
#     fields = "__all__"

#     def __unicode__(self):
#         return self.template_name

# def Detail(request, *args, **kwargs):
#     if request == "POST":
#         forms = Shorturl(urls = request.POST['longurl'], shortc=CreateShorturl())
#         formation =forms.save()
#         # so = Shorturl(forms)
#         return formation
#     return HttpResponse(f'{request.models.Shorturl.shorturl}')
 