from django.conf import settings
from django.conf.urls import include, url, patterns
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # ex: /posts/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<post_slug>[\w-]+)/$', views.detail, name='detail'),
    url(r'^tag/(?P<tag_slug>[\w-]+)/$', views.tag_view, name='tag_view'),
]

urlpatterns += patterns('',
    url(r'^comments/', include('fluent_comments.urls')),
)

if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT, 'show_indexes': True }),
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT, }),)
