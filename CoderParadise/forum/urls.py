from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^forum/(?P<id>\d+)/$', views.forum, name='forum'),
    url(r'^detail/(?P<id>\d+)/$', views.detail, name='detail'),
]