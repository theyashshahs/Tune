from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from music.models import Album, Song

@method_decorator(login_required, name='dispatch')
class IndexListView(generic.ListView):
    model = Album
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return super(IndexListView, self).get_queryset().filter(user=self.request.user)


class AlbumDetailView(generic.DetailView):
    model = Album
    template_name = 'music/album_detail.html'



class SongDetailView(generic.DetailView):
    model = Song
    template_name = 'music/song_detail.html'

    def get_queryset(self):
        return super(IndexListView, self).get_queryset().filter(user=self.request.user)


@method_decorator(login_required, name='dispatch')
class AlbumCreateView(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class AlbumUpdateView(UserPassesTestMixin, UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

    def test_func(self):
        album = self.get_object()

        if self.request.user == album.user:
            return True
    
        return False


@method_decorator(login_required, name='dispatch')
class AlbumDeleteView(UserPassesTestMixin, DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')

    def test_func(self):
        album = self.get_object()

        if self.request.user == album.user:
            return True
    
        return False


@method_decorator(login_required, name='dispatch')
class SongCreateView(CreateView):
    model = Song
    fields = ['album', 'song_title', 'audio_file']
    success_url = reverse_lazy('music:index')


@method_decorator(login_required, name='dispatch')
class SongUpdateView(UserPassesTestMixin, UpdateView):
    model = Song
    fields = ['album', 'song_title', 'audio_file']
    success_url = reverse_lazy('music:index')

    def test_func(self):
        album = self.get_object()

        if self.request.user == album.user:
            return True
    
        return False


@method_decorator(login_required, name='dispatch')
class SongDeleteView(UserPassesTestMixin, DeleteView):
    model = Song
    success_url = reverse_lazy('music:index')

    def test_func(self):
        album = self.get_object()

        if self.request.user == album.user:
            return True
    
        return False
