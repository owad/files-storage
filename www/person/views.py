from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, \
                                    UpdateView, DeleteView
from person.models import Client
from person.forms import ClientForm
 

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
    success_url = 'person_client_list'
    form_class = ClientForm
    
    def get_success_url(self):
        return reverse(self.success_url)

    
class ClientDelView(DeleteView):
    template_name = 'person/client/delete.html'
    model = Client
    success_url = 'person_client_list'
    
    def post(self, *args, **kwargs):
        self.delete(*args, **kwargs)
        return HttpResponseRedirect(reverse(self.success_url))
