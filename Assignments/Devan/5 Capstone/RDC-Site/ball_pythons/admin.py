from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django import forms

from .models import BallPython, Genetic

class BallPythonAdmin(admin.ModelAdmin):
    pass
    filter_horizontal = ('morph',)
    # formfield_overrides = {
    #     models.ManyToManyField: {'widget': CheckboxSelectMultiple}
    # }
    
class GeneticAdminForm(forms.ModelForm):
    ballpythons = forms.ModelMultipleChoiceField(
        queryset = BallPython.objects.all(),
        required = False,
        widget = FilteredSelectMultiple(
            verbose_name=_('BallPythons'),
            is_stacked = False
        )
    )

class GeneticAdmin(admin.ModelAdmin):
    ordering = ['gene']
    search_fields = ['genetics__gene']

admin.site.register(BallPython, BallPythonAdmin)
admin.site.register(Genetic, GeneticAdmin)