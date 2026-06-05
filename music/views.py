from django.shortcuts import render, redirect, get_object_or_404
from .models import Song, Playlist

def home(request):
    return render(request, "app/home.html")


def about(request):
    return render(request, "app/about.html")


def songs(request):
    songs = Song.objects.all()
    playlists = Playlist.objects.filter(user=request.user)

    return render(
        request,
        "app/song.html",
        {
            "songs": songs,
            "playlists": playlists,
        }
    )


def playlist(request):
    if request.method == "POST":
        name = request.POST.get("name")

        Playlist.objects.create(
            name=name,
            user=request.user
        )

        return redirect("playlist")

    playlists = Playlist.objects.filter(user=request.user)

    return render(
        request,
        "app/playlist.html",
        {
            "playlists": playlists
        }
    )


def add_song(request):
    if request.method == "POST":
        song_id = request.POST.get("song_id")
        playlist_id = request.POST.get("playlist_id")

        song = get_object_or_404(Song, id=song_id)
        playlist = get_object_or_404(
            Playlist,
            id=playlist_id,
            user=request.user
        )

        playlist.song.add(song)

    return redirect("song")


def playlist_detail(request, id):
    playlist = get_object_or_404(
        Playlist,
        id=id,
        user=request.user
    )

    return render(
        request,
        "app/playlist_detail.html",
        {"playlist": playlist}
    )

    return render(
        request,
        "app/playlist_detail.html",
        {
            "playlist": playlist
        }
    )