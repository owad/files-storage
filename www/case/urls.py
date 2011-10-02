from django.conf.urls.defaults import *
from case.views import CaseListView, CaseDetailsView, CaseAddView, \
                        CaseEditView, CaseDelView

urlpatterns = patterns('case.views',
    url(r'^details/(?P<pk>\d+)/$', CaseDetailsView.as_view(), name='case_details'),
    url(r'^list$', CaseListView.as_view(), name='case_list'),
    url(r'^add/(?P<client_id>\d*)$', CaseAddView.as_view(), name='case_add'),
    url(r'^edit/(?P<pk>\d+)/$', CaseEditView.as_view(), name='case_edit'),
    url(r'^delete/(?P<pk>\d+)/$', CaseDelView.as_view(), name='case_del'),
)
