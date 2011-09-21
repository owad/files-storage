from django.views.generic import View, TemplateView, ListView, \
    FormView as GenericFormView, ListView as GenericListView 
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import ProcessFormView
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, render
from django.core.urlresolvers import reverse
from django.forms import model_to_dict
from file.forms import FileForm
from file.models import File
from django.core.files.uploadedfile import UploadedFile
from settings import ALLOWED_ARCHIVES



class FormView(GenericFormView):
    template_name = 'file/form.html'
    form_class = FileForm
    success_url = 'file_list'
    initial = {}

class ListView(GenericListView):
    template_name = 'file/list.html'
    model = File
    paginate_by = 2
