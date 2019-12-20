from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = 'WebTune'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),  # landing page
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='details'),  # details of the songs
    # url(r'^(?P<album_id>[0-9]+)/favourite/$', views.favourite, name='favourite'),  # favourite function
]

urlpatterns += staticfiles_urlpatterns()

