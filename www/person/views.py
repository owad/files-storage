from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView, CreateView, \
                                    UpdateView, DeleteView
from person.models import Client, Agent
from person.forms import ClientForm, AgentForm
from django.shortcuts import get_object_or_404
 

class ClientListView(ListView):
    template_name = 'person/client/list.html'
    model = Client

class CilentDetailsView(DetailView):
    template_name = 'person/client/details.html'
    queryset = Client.objects.all()

class ClientAddView(CreateView):
    template_name = 'person/client/form.html'
    form_class = ClientForm
    
    def get_initial(self):
        self.initial['agent'] = self.request.user.id
        return self.initial
    
    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('person_client_list'))
    
    
class ClientEditView(UpdateView):
    template_name = 'person/client/form.html'
    queryset = Client.objects.all()
    success_url = 'person_client_details'
    form_class = ClientForm
    
    def get_success_url(self):
        return reverse(self.success_url, kwargs={'pk': self.get_object().id})

    
class ClientDelView(DeleteView):
    template_name = 'person/client/delete.html'
    model = Client
    success_url = 'person_client_list'
    
    def post(self, *args, **kwargs):
        self.delete(*args, **kwargs)
        return HttpResponseRedirect(reverse(self.success_url))
    
class AgentDetailsView(TemplateView):
    template_name = 'person/agent/details.html'
    
    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        context['agent'] = Agent.objects.get(user=self.request.user)
        return context
    
class AgentEditView(UpdateView):
    template_name = 'person/agent/form.html'
    queryset = Agent.objects.all()
    success_url = 'person_agent_details'
    form_class = AgentForm
    
    def get_object(self, queryset=None):
        return Agent.objects.get(user=self.request.user)
    
    def get_success_url(self):
        return reverse(self.success_url)
    