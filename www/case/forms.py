from django.forms import ModelForm
from case.models import Case

class CaseForm(ModelForm):
    class Meta:
        model = Case
