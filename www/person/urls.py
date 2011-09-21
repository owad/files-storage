from django.conf.urls.defaults import *
from person.views import ClientListView, ClientFormView, AgentFormView

urlpatterns = patterns('person.views',
    url(r'^client/list$', ClientListView.as_view(), name='person_client_list'),
    url(r'^client/form$', ClientFormView.as_view(), name='person_client_form'),
    url(r'^agent/form$', AgentFormView.as_view(), name='person_agent_form'),
)
