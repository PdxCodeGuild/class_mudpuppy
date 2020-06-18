from django import forms
from django.forms import ModelForm


from .models import *


class ItemForm(forms.ModelForm):
    
    class Meta:
        model = Todo
        fields = '__all__'
