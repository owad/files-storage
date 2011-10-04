from django.forms import ModelForm
from django.forms.widgets import HiddenInput
from person.models import Employee, Client

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        exclude = {'user'}

class ClientForm(ModelForm):
    class Meta:
        model = Client
        widgets = {'employee': HiddenInput()}
