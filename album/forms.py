from django import forms
from .models import AlbumModel


class AlbumForm(forms.ModelForm):

    class Meta:
        model = AlbumModel
        fields = ["album_name", "musician", "release_date", "rating"]
        RATING_CHOICES = [
            (1, "1 Star"),
            (2, "2 Stars"),
            (3, "3 Stars"),
            (4, "4 Stars"),
            (5, "5 Stars"),
        ]
        widgets = {
            "release_date": forms.DateInput(attrs={"type": "date"}),
            "rating": forms.Select(choices=RATING_CHOICES),
        }
