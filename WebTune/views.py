from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from WebTune.models import Album, Song


class IndexView(generic.ListView):
    template_name = 'WebTune/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class AlbumDetailView(generic.DetailView):
    model = Album
    template_name = 'WebTune/album_detail.html'


class SongDetailView(generic.DetailView):
    model = Song
    template_name = 'WebTune/song_detail.html'


class AlbumCreateView(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']
    success_url = reverse_lazy('WebTune:index')


class AlbumUpdateView(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']
    success_url = reverse_lazy('WebTune:index')


class AlbumDeleteView(DeleteView):
    model = Album
    success_url = reverse_lazy('WebTune:index')


class SongCreateView(CreateView):
    model = Song
    fields = ['album', 'song_title', 'audio_file']
    success_url = reverse_lazy('WebTune:index')


class SongUpdateView(UpdateView):
    model = Song
    fields = ['album', 'song_title', 'audio_file']
    success_url = reverse_lazy('WebTune:index')


class SongDeleteView(DeleteView):
    model = Song
    success_url = reverse_lazy('WebTune:index')
