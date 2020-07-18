from django.shortcuts import render
from .models import Vineyard, Reservation, Contact
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

def index(request):
    context={"Vineyards": Vineyard.objects.all()}
    return render(request, 'wine_tours/pnwwt.html', context)

def vineyard_detail(request, vineyard_pk):
    context={"vineyard": Vineyard.objects.get(pk=vineyard_pk)}
    return render(request,'wine_tours/detail.html', context)

def receive_reservation(request):
    print(request.POST)
    new_reservation=Reservation (
        user= request.user, 
        party_size= request.POST ["size"],
        vineyard_id= request.POST ["vineyard_id"],
    )
    new_reservation.save()
    return HttpResponseRedirect("/wine/")

def receive_contact(request):
    new_contact=Contact (
    user= request.user, 
    text= request.POST["contact"],
    )
    new_contact.save()
    return HttpResponseRedirect("/wine/")

@login_required
def contact(request):
    return render(request, 'wine_tours/contact.html', None)

@login_required
def make_reservation(request, vineyard_pk):
    context={"vineyard": Vineyard.objects.get(pk=vineyard_pk)}
    return render(request, 'wine_tours/reservation.html', context)


# Create your views here.