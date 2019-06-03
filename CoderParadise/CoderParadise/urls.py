"""CoderParadise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from django.conf import settings

urlpatterns = [
    path(r'', include("home.urls")),
    path(r'admin/', admin.site.urls),
    path(r'QA/', include("QA.urls")),
    path(r'register/', user_views.register, name='register'),
    path(r'logout/', user_views.logout_request, name='logout'),
    path(r'login/', user_views.login_request, name='login'),
    path(r'users/', include("users.urls")),
    path(r'forum/', include("forum.urls")),
]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

