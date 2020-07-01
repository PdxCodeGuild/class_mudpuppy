from django.shortcuts import render
from django.http import HttpResponse
from .models import Song #, Mus_Tags, NonMus_Tags

# Create your views here.
def index(request):
    song_list = Song.objects.all()
    context = {
        'song_list_dict': song_list,
    }
    return render(request, 'capstone/index.html', context)

def add_song(request):
    data = request.POST
    new_song = Song(
        song_name = data['song_name'],
        artist_name = data['artist_name'],
        release_year = data['release_year'],
        spotify_link = data['spotify_link'],
        chords_link = data['chords_link'],
        info_link = data['info_link'],
    )
    new_song.save()

    return HttpResponse(new_song.song_name)