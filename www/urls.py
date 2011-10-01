from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from www import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^file/', include('file.urls')),
    url(r'^case/', include('case.urls')),
    url(r'^', include('person.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )