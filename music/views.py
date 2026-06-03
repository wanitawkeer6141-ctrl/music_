from django.shortcuts import render
from .models import Song

# Create your views here.

def home(request):
    return render(request,'app/home.html')
def songs(request):
   
    songs = Song.objects.all()
    return render(request,'app/song.html',{'songs':songs})

def about(request):
    return render(request,'app/about.html')
