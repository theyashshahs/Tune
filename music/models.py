from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Album(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return f'{self.user} {self.album_title}'

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.album_logo.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.album_logo.path)

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='audio/', blank=True)
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title