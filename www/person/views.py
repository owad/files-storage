from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
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
    
#    def get_initial(self):
#        self.initial = GenericFormView.get_initial(self)
#        return self.initial
    
    def form_valid(self, form):
        new_client = form.save(commit=False)
        new_client.agent_id = self.request.user.id
        new_client.save()
        return HttpResponseRedirect(reverse('person_client_list'))
    
class AgentFormView(GenericFormView):
    template_name = 'person/agent/form.html'
    form_class = AgentForm
    success_url = 'person_agent_form'
    initial = {}