from django.views.generic import View, TemplateView, ListView, DetailView
from django.views.generic.edit import ProcessFormView
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, render
from django.core.urlresolvers import reverse
from django.forms import model_to_dict
from upload.forms import FileForm
from upload.models import File
from django.core.files.uploadedfile import UploadedFile
from settings import ALLOWED_ARCHIVES

class EditFile(TemplateView):
    template_name = 'upload/form.html'
    
    def get_context_data(self, **kwargs):
        context = super(EditFile, self).get_context_data(**kwargs)
        context['file_form'] = FileForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            content_type = form.files['file'].content_type
            saved_file = form.save()
            saved_file.content_type = content_type
            saved_file.save()
            return HttpResponseRedirect(reverse('upload_new'))
        else:
            return self.get(request, *args, **kwargs)

class FilesList(ListView):
    template_name = 'upload/list.html'
    model = File
    paginate_by = 2
