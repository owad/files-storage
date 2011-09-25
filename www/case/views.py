from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.core.exceptions import ImproperlyConfigured
    
from django.core.urlresolvers import reverse

from django.views.generic.create_update import create_object

from case.models import Case
from case.forms import CaseForm
from person.models import Agent

class CaseListView(ListView):
    template_name = 'case/list.html'
    model = Case
    
class CaseAddView(CreateView):
    template_name = 'case/form.html'
    form_class = CaseForm
    
    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('case_list'))
    
    
class CaseEditView(UpdateView):
    template_name = 'case/form.html'
    queryset = Case.objects.all()
    success_url = 'case_list'
    
    def get_success_url(self):
        if self.success_url:
            url = reverse(self.success_url)
        else:
            raise ImproperlyConfigured(
                "No URL to redirect to. Provide a success_url.")
        return url
    
class CaseDelView(DeleteView):
    template_name = 'case/delete.html'
    model = Case
    success_url = 'case_list'
    
    def post(self, *args, **kwargs):
        self.delete(*args, **kwargs)
        return HttpResponseRedirect(reverse(self.success_url))
