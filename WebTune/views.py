from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from WebTune.models import Album, Song
from WebTune.forms import UserForm


class IndexView(generic.ListView):
    template_name = 'tune/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class UserView(View):
    form_class = UserForm
    template_name = 'tune/register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)

            if user.is_active:
                login(request, user)
                return redirect('tune:index')

        return render(request, self.template_name, {'form': form})

class AlbumDetailView(generic.DetailView):
    model = Album
    template_name = 'tune/album_detail.html'


class SongDetailView(generic.DetailView):
    model = Song
    template_name = 'tune/song_detail.html'


class AlbumCreateView(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']
    success_url = reverse_lazy('tune:index')


class AlbumUpdateView(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']
    success_url = reverse_lazy('tune:index')


class AlbumDeleteView(DeleteView):
    model = Album
    success_url = reverse_lazy('tune:index')


class SongCreateView(CreateView):
    model = Song
    fields = ['album', 'song_title', 'audio_file']
    success_url = reverse_lazy('tune:index')


class SongUpdateView(UpdateView):
    model = Song
    fields = ['album', 'song_title', 'audio_file']
    success_url = reverse_lazy('tune:index')


class SongDeleteView(DeleteView):
    model = Song
    success_url = reverse_lazy('tune:index')
