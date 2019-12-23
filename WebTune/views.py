from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from WebTune.models import Album, Song


class IndexView(generic.ListView):
    template_name = 'WebTune/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'WebTune/details.html'


class AlbumCreateView(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']
