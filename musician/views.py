from django.shortcuts import render, redirect
from . import forms, models
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
def musician(request):
    if request.method == "POST":
        musicianForm = forms.MusicianForm(request.POST)
        if musicianForm.is_valid():
            musicianForm.save()
            return redirect("homepage")
    else:
        musicianForm = forms.MusicianForm()

    return render(request, "musician.html", {"form": musicianForm})

class musicianCreateView(CreateView):
    model = models.MusicianModel
    form_class = forms.MusicianForm
    template_name = "musician.html"
    success_url = reverse_lazy("homepage")
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def EditMusician(request, id):
    data = models.MusicianModel.objects.get(pk=id)
    musicianForm = forms.MusicianForm(instance=data)
    if request.method == "POST":
        musicianForm = forms.MusicianForm(request.POST, instance=data)
        if musicianForm.is_valid():
            musicianForm.save()
            return redirect("homepage")

    return render(request, "musician.html", {"form": musicianForm})

class EditMusicianUpdateView(UpdateView):
    model = models.MusicianModel
    form_class = forms.MusicianForm
    template_name = "musician.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("homepage")

def DeleteMusician(request, id):
    data = models.MusicianModel.objects.get(pk=id)
    data.delete()
    return redirect("homepage")


class DeleteMusicianView(DeleteView):
    model = models.MusicianModel
    template_name = "delete.html"
    success_url = reverse_lazy("homepage")
    pk_url_kwarg = "id"
