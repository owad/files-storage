from django.forms import ModelForm
from django.forms.widgets import HiddenInput
from person.models import Agent, Client

class AgentForm(ModelForm):
    class Meta:
        model = Agent

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = {'title', 'first_name', 'last_name', 'company_name', 'email', 
                  'address_line_1', 'address_line_2', 'city', 'postcode'}