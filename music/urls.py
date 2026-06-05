from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("song/", views.songs, name="song"),
    path("about/", views.about, name="about"),

    path("playlist/", views.playlist, name="playlist"),

    path("add-song/", views.add_song, name="add_song"),

    path(
        "playlist/<int:id>/",
        views.playlist_detail,
        name="playlist_detail"
    ),
]