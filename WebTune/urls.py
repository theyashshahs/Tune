from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = 'WebTune'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),  # landing page
    url(r'^album/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),  # details of the songs
    url(r'^album/add/$', views.AlbumCreateView.as_view(), name='album-add'),  # album addition view
]

urlpatterns += staticfiles_urlpatterns()

