from django.conf.urls.defaults import *
from www.upload.views import *

urlpatterns = patterns('upload.views',
    url(r'^$', FilesList.as_view(), name='upload_list'),
    url(r'^edit/(?P<pk>\d+)$', EditFile.as_view(), name='upload_edit'),
    url(r'^add$', EditFile.as_view(), name='upload_add'),
)
