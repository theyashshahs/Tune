from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from . import views


app_name = 'WebTune'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),  # landing page
    url(r'^album/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),  # details of the songs
    url(r'^album/add/$', views.AlbumCreateView.as_view(), name='album-add'),  # album addition view
    url(r'^album/update/(?P<pk>[0-9]+)/', views.AlbumUpdateView.as_view(), name='album-update'),
    url(r'^album/(?P<pk>[0-9]+)/delete/', views.AlbumDeleteView.as_view(), name='album-delete'),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
