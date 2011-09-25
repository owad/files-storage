from django.conf.urls.defaults import *
from person.views import ClientListView, ClientAddView, ClientEditView, \
                        ClientDelView

urlpatterns = patterns('person.views',
    url(r'^client/list$', ClientListView.as_view(), name='person_client_list'),
    url(r'^client/add$', ClientAddView.as_view(), name='person_client_add'),
    url(r'^client/edit/(?P<pk>\d+)/$', ClientEditView.as_view(), name='person_client_edit'),
    url(r'^client/delete/(?P<pk>\d+)/$', ClientDelView.as_view(), name='person_client_del')
)
