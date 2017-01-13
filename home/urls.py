from django.conf.urls import url, include
from django.views.generic.base import RedirectView

from .views import IndexView, PhotoView

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/')),
    url(r'^index/$', IndexView.as_view(), name='index'),
]
