from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, \
                                    UpdateView, DeleteView

from case.models import Case
from case.forms import CaseForm
from person.models import Client

class CaseDetailsView(DetailView):
    template_name = 'case/details.html'
    queryset = Case.objects.all()
    
class CaseListView(ListView):
    template_name = 'case/list.html'
    model = Case
    
class CaseAddView(CreateView):
    template_name = 'case/form.html'
    form_class = CaseForm
    success_url = 'case_details'
    
    def get_context_data(self, **kwargs):
        context = CreateView.get_context_data(self, **kwargs)
        context['client'] = get_object_or_404(Client, pk=self.kwargs['client_id'])
        return context
    
    def get_initial(self):
        initial = CreateView.get_initial(self)
        initial['client'] = self.get_context_data()['client']
        return initial
    
    def form_valid(self, form):
        new_case = form.save()
        return HttpResponseRedirect(reverse(self.success_url, kwargs={'pk': new_case.id}))
    
class CaseEditView(UpdateView):
    template_name = 'case/form.html'
    queryset = Case.objects.all()
    success_url = 'case_details'
    form_class = CaseForm
    
    def get_context_data(self, **kwargs):
        context = UpdateView.get_context_data(self, **kwargs)
        context['client'] = self.get_object().client
        return context
    
    def get_success_url(self):
        return reverse(self.success_url, kwargs={'pk': self.get_object().id})
    
class CaseDelView(DeleteView):
    template_name = 'case/delete.html'
    model = Case
    success_url = 'case_list'
    
    def post(self, *args, **kwargs):
        self.delete(*args, **kwargs)
        return HttpResponseRedirect(reverse(self.success_url))
