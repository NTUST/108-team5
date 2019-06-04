from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^findMyForum/(?P<username>[\w\-]+)/$', views.findMyForum, name='findMyForum'),
    url(r'^detail/(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'^create/', views.create, name='create'),
    url(r'^update/(?P<id>\d+)/$', views.update, name='update'),
    url(r'^thumb/(?P<id>\d+)/$', views.thumb, name='thumb'),
    url(r'^delete/(?P<id>\d+)/$', views.delete, name='delete'),
]