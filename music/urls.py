from django.conf.urls import url
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views


app_name = 'music'

# urlpatterns = [
#     path('/', views.IndexListView.as_view(), name='index'),
#     path('album/<int:pk>/', views.AlbumDetailView.as_view(), name='album-detail'),
#     path('album/add/', views.AlbumCreateView.as_view(), name='album-add'),
#     path('album/update/<int:pk>/', views.AlbumUpdateView.as_view(), name='album-update'),
#     path('album/<int:pk>/delete/', views.AlbumDeleteView.as_view(), name='album-delete'),
#     path('song/add/', views.SongCreateView.as_view(), name='song-add'),
#     path('song/update/<int:pk>/', views.SongUpdateView.as_view(), name='song-update'),
#     url('song/<int:pk>/delete/', views.SongDeleteView.as_view(), name='song-delete')
# ]

urlpatterns = [
    url(r'^$', views.IndexListView.as_view(), name='index'),  
    url(r'^album/(?P<pk>[0-9]+)/$', views.AlbumDetailView.as_view(),
        name='album-detail'),  
    url(r'^album/add/$', views.AlbumCreateView.as_view(),
        name='album-add'),  
    url(r'^album/update/(?P<pk>[0-9]+)/',
        views.AlbumUpdateView.as_view(), name='album-update'),
    url(r'^album/(?P<pk>[0-9]+)/delete/',
        views.AlbumDeleteView.as_view(), name='album-delete'),
    url(r'^song/add/$', views.SongCreateView.as_view(), name='song-add'),
    url(r'^song/update/(?P<pk>[0-9]+)/',
        views.SongUpdateView.as_view(), name='song-update'),
    url(r'^song/(?P<pk>[0-9]+)/delete/',
        views.SongDeleteView.as_view(), name='song-delete')
]

urlpatterns += staticfiles_urlpatterns()

