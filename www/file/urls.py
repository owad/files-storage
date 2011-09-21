from django.conf.urls.defaults import *
from file.views import FormView, ListView

urlpatterns = patterns('upload.views',
    url(r'^list$', ListView.as_view(), name='file_list'),
    url(r'^form$', FormView.as_view(), name='file_form'),
)
