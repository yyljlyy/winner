from django.conf.urls import patterns, include, url

from django.contrib import admin
from winner import settings
from winner.views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'winner.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^info/', add_user),
    url(r'^delete/', delete_user),
    url(r'^update/', update_user),
    url(r'^deleteo/', delete_ouser),
    url(r'^updateo/', update_ouser),
    url(r'^(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.TEMPLATE_DIRS}),
    url(r'^admin/', include(admin.site.urls)),
)
