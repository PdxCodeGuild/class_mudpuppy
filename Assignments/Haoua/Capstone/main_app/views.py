from django.shortcuts import render

# Create youmr views here.
def home(request):
    return render(request,'main_app/landing.html')
    


