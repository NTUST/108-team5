from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^findMyOA/(?P<username>[\w\-]+)/$', views.findMyOA, name='findMyOA'),
    url(r'^detail/(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'^create', views.create, name='create'),
]