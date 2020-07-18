from django import forms
from .models import TodoItem

class TodoForm(forms.Form):
    todo_text = forms.CharField(label='Todo Text', max_length=100)
