from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views


app_name = 'tune'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),  # landing page
    # url(r'^register/$', views.UserView.as_view(), name='register'), # registration form
    url(r'^album/(?P<pk>[0-9]+)/$', views.AlbumDetailView.as_view(), name='album-detail'),  # details of the albums
    url(r'^album/add/$', views.AlbumCreateView.as_view(), name='album-add'),  # album addition view
    url(r'^album/update/(?P<pk>[0-9]+)/', views.AlbumUpdateView.as_view(), name='album-update'),
    url(r'^album/(?P<pk>[0-9]+)/delete/', views.AlbumDeleteView.as_view(), name='album-delete'),
    url(r'^song/add/$', views.SongCreateView.as_view(), name='song-add'),
    url(r'^song/update/(?P<pk>[0-9]+)/', views.SongUpdateView.as_view(), name='song-update'),
    url(r'^song/(?P<pk>[0-9]+)/delete/', views.SongDeleteView.as_view(), name='song-delete')
]

urlpatterns += staticfiles_urlpatterns()
