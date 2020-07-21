from django.forms import ModelForm, 
from .models import PersonComplaint
class ComplaintForm(forms.ModelForm):
    class Meta:
        model = PersonComplaint
        fields = '__all__'