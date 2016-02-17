from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /posts/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<post_slug>[-_\w]+)/$', views.detail, name='detail'),
]