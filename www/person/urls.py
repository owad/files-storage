from django.conf.urls.defaults import *
from person.views import ClientListView, ClientAddView, ClientEditView, \
                        ClientDelView, CilentDetailsView, \
                        AgentDetailsView, AgentEditView

urlpatterns = patterns('person.views',
    url(r'^$', ClientListView.as_view(), name='person_client_list'),
    url(r'^client/details/(?P<pk>\d+)/$', CilentDetailsView.as_view(), name='person_client_details'),
    url(r'^client/add$', ClientAddView.as_view(), name='person_client_add'),
    url(r'^client/edit/(?P<pk>\d+)/$', ClientEditView.as_view(), name='person_client_edit'),
    url(r'^client/delete/(?P<pk>\d+)/$', ClientDelView.as_view(), name='person_client_del'),
    url(r'^agent/details$', AgentDetailsView.as_view(), name='person_agent_details'),
    url(r'^agent/edit$', AgentEditView.as_view(), name='person_agent_edit'),
)
