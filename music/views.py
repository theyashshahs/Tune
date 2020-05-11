from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from music.models import Album, Song
from music.forms import UserForm


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

class AlbumDetailView(generic.DetailView):
    model = Album
    template_name = 'music/album_detail.html'


class SongDetailView(generic.DetailView):
    model = Song
    template_name = 'music/song_detail.html'


@method_decorator(login_required, name='dispatch')
class AlbumCreateView(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']
    success_url = reverse_lazy('music:index')


@method_decorator(login_required, name='dispatch')
class AlbumUpdateView(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']
    success_url = reverse_lazy('music:index')


@method_decorator(login_required, name='dispatch')
class AlbumDeleteView(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


@method_decorator(login_required, name='dispatch')
class SongCreateView(CreateView):
    model = Song
    fields = ['album', 'song_title', 'audio_file']
    success_url = reverse_lazy('music:index')


@method_decorator(login_required, name='dispatch')
class SongUpdateView(UpdateView):
    model = Song
    fields = ['album', 'song_title', 'audio_file']
    success_url = reverse_lazy('music:index')


@method_decorator(login_required, name='dispatch')
class SongDeleteView(DeleteView):
    model = Song
    success_url = reverse_lazy('music:index')
