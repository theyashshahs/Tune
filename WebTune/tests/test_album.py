from django.test import TestCase
from WebTune.models import Album


class AlbumTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        Album.objects.create(
            artist='Optimus', album_title='Power is love', genre='Pop')

    def artist_name_label(self):
        artist = Album.objects.get(id=1)
        field_label = artist._meta.get_field('artist').verbose_name
        self.assertEquals(field_label, 'artist')

    def artist_name_max_length(self):
        artist = Album.objects.get(id=1)
        max_length = artist._meta.get_field('artist').max_length
        self.assertEquals(max_length, 250)
