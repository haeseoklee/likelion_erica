"""likelion_erica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views

from django.conf import settings
from django.conf.urls.static import static

from home.views import IndexView, UserRegisterView
from home.forms import UserAuthenticationForm

urlpatterns = [
    #url(r'^', include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^home/', include('home.urls', namespace='home')),
    url(r'^apply/', include('resumes.urls', namespace='apply')),
    url(r'^login/$', views.login, {
        'template_name': 'registration/login.html',
        'authentication_form': UserAuthenticationForm,
        }, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', UserRegisterView.as_view(), name='register'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
