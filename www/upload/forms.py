from django.forms import ModelForm
from django.forms.widgets import HiddenInput
from www.upload.models import File

class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ('id', 'title', 'file')
        widgets = {
           'id': HiddenInput(),
           'content_type': HiddenInput()
        }
