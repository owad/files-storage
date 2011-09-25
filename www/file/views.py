from django.views.generic import View, TemplateView, ListView, \
    FormView as GenericFormView, ListView as GenericListView 
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, \
                                    UpdateView, DeleteView
from file.forms import FileForm
from file.models import File
from case.models import Case

class FileAddView(CreateView):
    template_name = 'file/form.html'
    form_class = FileForm

    def get_initial(self):
        self.initial['case'] = get_object_or_404(Case, pk=self.kwargs['case_id'])
        return self.initial

    def form_valid(self, form):
        new_file = form.save(commit=False)
        new_file.case = self.case
        new_file.save()
        return HttpResponseRedirect(reverse('case_details', kwargs={'pk': new_file.case.id }))
    
class FileListView(ListView):
    template_name = 'file/list.html'
    model = File
    paginate_by = 2

class FileDelView(DeleteView):
    template_name = 'file/delete.html'
    model = File
    success_url = 'case_details'
    
    def post(self, *args, **kwargs):
        self.delete(*args, **kwargs)
        return HttpResponseRedirect(reverse(self.success_url, kwargs={'pk': self.get_object().case.id }))