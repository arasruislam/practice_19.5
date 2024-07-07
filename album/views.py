from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from . import forms, models
from django.urls import reverse_lazy

# Create your views here.
def Album(request):
    if request.method=="POST":
        albumForm = forms.AlbumForm(request.POST)
        if albumForm.is_valid():
            albumForm.save()
            return redirect("homepage")
    else:
        albumForm = forms.AlbumForm()

    return render(request,"album.html", {"form": albumForm})


class albumCreateView(CreateView):
    model = models.AlbumModel
    form_class = forms.AlbumForm
    template_name = "album.html"
    success_url = reverse_lazy("homepage")

def EditAlbum(request, id):
    data = models.AlbumModel.objects.get(pk=id)
    print(data)
    albumForm = forms.AlbumForm(instance=data)
    if request.method == "POST":
        albumForm = forms.AlbumForm(request.POST, instance=data)
        if albumForm.is_valid():
            albumForm.save()
            return redirect("homepage")

    return render(request, "album.html", {"form": albumForm})


class EditAlbumUpdateView(UpdateView):
    model = models.AlbumModel
    form_class = forms.AlbumForm
    template_name = "album.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("homepage")
