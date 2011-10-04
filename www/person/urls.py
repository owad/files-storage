from django.conf.urls.defaults import *
from person.views import ClientListView, ClientAddView, ClientEditView, \
                        ClientDelView, CilentDetailsView, \
                        EmployeeDetailsView, EmployeeEditView

urlpatterns = patterns('person.views',
    url(r'^$', ClientListView.as_view(), name='person_client_list'),
    url(r'^client/details/(?P<pk>\d+)/$', CilentDetailsView.as_view(), name='person_client_details'),
    url(r'^client/add$', ClientAddView.as_view(), name='person_client_add'),
    url(r'^client/edit/(?P<pk>\d+)/$', ClientEditView.as_view(), name='person_client_edit'),
    url(r'^client/delete/(?P<pk>\d+)/$', ClientDelView.as_view(), name='person_client_del'),
    url(r'^employee/details$', EmployeeDetailsView.as_view(), name='person_employee_details'),
    url(r'^employee/edit$', EmployeeEditView.as_view(), name='person_employee_edit'),
)
