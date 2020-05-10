from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = 'users'

urlpatterns = [
    url(r'^register/', views.registration, name='register'),
]