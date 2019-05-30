from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^profile/(?P<username>[\w\-]+)/$', views.profile, name='profile'),
]