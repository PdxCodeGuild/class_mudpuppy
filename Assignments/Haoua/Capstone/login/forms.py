from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Register(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        # he user mdel will be affected
        model = User
        # attributes in the order we want them in
        fields = ['username', 'email',]