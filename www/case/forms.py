from django.forms import ModelForm
from django.forms.widgets import HiddenInput
from case.models import Case
from tinymce.widgets import TinyMCE


class CaseForm(ModelForm):
    class Meta:
        model = Case
        widgets = {
               'client': HiddenInput(), 
               'notes': TinyMCE(attrs={
                    'cols': 80, 
                    'rows': 20
                }, 
                mce_attrs={
                   'language': 'en',
                   'theme': 'advanced'
               })}
