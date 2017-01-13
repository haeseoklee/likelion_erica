from django.conf.urls import url
from .views import (
    model_form_upload,
    ApplyView,
    )

urlpatterns = [
    url(r'^$', ApplyView.as_view(url='submit/'), name='apply'),
    url(r'^submit/$', model_form_upload, name='submit'),
]
