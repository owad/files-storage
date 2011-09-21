from django.conf.urls.defaults import *
from case.views import FormView, ListView

urlpatterns = patterns('case.views',
    url(r'^list$', ListView.as_view(), name='case_list'),
    url(r'^form$', FormView.as_view(), name='case_form'),
)
