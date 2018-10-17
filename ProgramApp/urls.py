from django.conf.urls import url
from .views import programIndex, programUpdate

urlpatterns = [
    url(r'^$', programIndex, name='programIndex'),
    url(r'(?P<id>[-\w]+)/$', programUpdate, name='programUpdate')
]