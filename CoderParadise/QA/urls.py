from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'^create', views.create, name='create'),
]