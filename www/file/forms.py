from django.forms import ModelForm
from django.forms.widgets import HiddenInput
from file.models import File

class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ('id', 'title', 'file', 'case')
        widgets = {'case': HiddenInput()}
