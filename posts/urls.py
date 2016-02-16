from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /posts/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<post_id>[0-9]+)/$', views.detail, name='detail'),
]