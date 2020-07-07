from django.shortcuts import render

# Create youmr views here.
def home(request):
    render(request,"landing.html")


