from django.urls import path
from . import views

urlpatterns = [
    path("", views.musicianCreateView.as_view(), name="musician"),
    path("delete/<int:id>", views.DeleteMusicianView.as_view(), name="DeleteMusician"),
    path("edit/<int:id>", views.EditMusicianUpdateView.as_view(), name="EditMusician"),
]
