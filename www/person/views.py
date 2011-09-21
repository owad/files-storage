from django.views.generic import ListView as GenericListView, \
    FormView as GenericFormView
from person.models import Client, Agent
from person.forms import AgentForm, ClientForm
 

class ClientListView(GenericListView):
    template_name = 'person/client/list.html'
    model = Client

class ClientFormView(GenericFormView):
    template_name = 'person/client/form.html'
    form_class = ClientForm
    success_url = 'person_client_form'
    
    def get_initial(self):
        self.initial = GenericFormView.get_initial(self)
        self.initial['agent'] = Agent.objects.get(user=self.request.user)
        return self.initial
    
class AgentFormView(GenericFormView):
    template_name = 'person/agent/form.html'
    form_class = AgentForm
    success_url = 'person_agent_form'
    initial = {}