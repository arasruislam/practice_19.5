from django.shortcuts import render
from album.models import AlbumModel


def home(request):
    data = AlbumModel.objects.all()
    print(data)
    return render(request, "index.html", {"data": data})
