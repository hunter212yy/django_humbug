from django.conf.urls import include, url, patterns

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