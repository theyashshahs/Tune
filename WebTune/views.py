from django.shortcuts import render, get_object_or_404
from .models import Album, Song
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'WebTune/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'WebTune/details.html'


# def favourite(request, album_id):
#     album = get_object_or_404(Album, pk=album_id)  # obtaining album
#     # print(request.POST['song'])
#     try:
#         selected_song = album.song_set.get(pk=request.POST['song'])
#         selected_song.is_favourite = True
#         selected_song.save()
#         return render(request, 'WebTune/details.html', {'album': album})  # adds songs to favourite list
#
#     except (KeyError, Song.DoesNotExist):
#         return render(request, 'WebTune/details.html', {
#             'album': album,
#             'error_message': "You did not select a valid song",
#         })
