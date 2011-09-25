from django.conf.urls.defaults import *
from file.views import FileListView, FileAddView, FileDelView, FileDetailsView

urlpatterns = patterns('upload.views',
    url(r'^list$', FileListView.as_view(), name='file_list'),
    url(r'^add/(?P<case_id>\d*)/$', FileAddView.as_view(), name='file_add'),
    url(r'^details/(?P<pk>\d+)/$', FileDetailsView.as_view(), name='file_details'),
    url(r'^delete/(?P<pk>\d+)/$', FileDelView.as_view(), name='file_del')
)
