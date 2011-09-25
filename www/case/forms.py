from django.forms import ModelForm
from django.forms.widgets import HiddenInput
from case.models import Case

class CaseForm(ModelForm):
    class Meta:
        model = Case
