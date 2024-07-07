from django.urls import path
from . import views

urlpatterns = [
    path("", views.albumCreateView.as_view(), name="album"),
    path("delete/<int:id>", views.EditAlbumUpdateView.as_view(), name="EditAlbum"),
]
