from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from music.validators import validate_audio_extension, validate_image_extension


class Album(models.Model):
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE)
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.ImageField(upload_to='images/', blank=True, default='audio/default.jpg', validators=[validate_image_extension])

    def __str__(self):
        return f'{self.user} {self.album_title}'

    def get_absolute_url(self):
        return reverse('music:album-detail', kwargs={'pk': self.pk})


class Song(models.Model):
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='audio/', blank=True, default='audio/default.jpg', validators=[validate_audio_extension])

    def __str__(self):
        return self.song_title
