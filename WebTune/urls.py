from django.conf.urls import url
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = 'WebTune'

urlpatterns = [
    url(r'^$', views.index, name='index'),  # landing page
    url(r'^(?P<album_id>[0-9]+)/$', views.details, name='details'),  # details of the songs
    url(r'^(?P<album_id>[0-9]+)/favourite/$', views.favourite, name='favourite'),  # favourite function
]

urlpatterns += staticfiles_urlpatterns()
