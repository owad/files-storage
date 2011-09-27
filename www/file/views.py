from django.views.generic import View, TemplateView, ListView, \
    FormView as GenericFormView, ListView as GenericListView 
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, \
                                    UpdateView, DeleteView

from PIL import Image

from file.forms import FileForm
from file.models import File
from case.models import Case


class FileDetailsView(DetailView):
    template_name = 'file/details.html'
    queryset = File.objects.all()

class FileAddView(CreateView):
    template_name = 'file/form.html'
    form_class = FileForm

    def get_context_data(self, **kwargs):
        context = super(FileAddView, self).get_context_data(**kwargs)
        context['case'] = get_object_or_404(Case, pk=self.kwargs['case_id'])
        return context

    def get_initial(self):
        self.initial['case'] = self.get_context_data()['case']
        return self.initial

    def form_valid(self, form):
        new_file = form.save(commit=False)
        new_file.case = self.get_initial()['case']
        new_file.size = self.request.FILES['file'].size
        new_file.content_type = self.request.FILES['file'].content_type
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
        case = self.get_object().case
        self.delete(*args, **kwargs)
        return HttpResponseRedirect(reverse(self.success_url, kwargs={'pk': case.id }))
    
class FileServeView(TemplateView):
    
    def render_to_response(self, context, **response_kwargs):
        file = get_object_or_404(File, pk=self.kwargs['pk'])
        if file.case.client.agent.id != self.request.user.id:
            pass # return default image 
        image_data = open(str(file.file), "rb").read()
        return HttpResponse(image_data, mimetype="image/png")
    
    