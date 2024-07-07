from django.db import models
from musician.models import MusicianModel


# Create your models here.
class AlbumModel(models.Model):
    album_name = models.CharField(max_length=50)
    musician = models.ForeignKey(MusicianModel, on_delete=models.CASCADE)
    release_date = models.DateField()
    rating = models.CharField(max_length=5)

    def __str__(self) -> str:
        return self.album_name
