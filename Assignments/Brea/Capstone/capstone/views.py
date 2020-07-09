from django.shortcuts import render
from django.http import HttpResponse
from .models import Song, Artist, Tags, SongReview #, Mus_Tags, NonMus_Tags

# Create your views here.
def index(request):
    song_list = Song.objects.all()
    context = {
        'song_list_dict': song_list,
        'choices': Tags.Genres.choices,
    }
    return render(request, 'capstone/index.html', context)

def add_song(request):
    data = request.POST
    print(data)
    new_song = Song(
        song_name = data['song_name'],
        release_year = data['release_year'],
        # spotify_link = data['spotify_link'],
        # chords_link = data['chords_link'],
        # info_link = data['info_link'],

        # genre = data['genre'],
        tempo = data['tempo'],
        singability = data['singability'],
        playability = data['playability'],
        repetition = data['repetition'],
        arousal = data['arousal'],
        popularity = data['popularity'],
        valence = data['valence'],
        comments = data['comment'],
    )
    artists = data['artist']
    new_song.save()

    for artist in artists.split(';'):
        new_song.artist.add(
            Artist.objects.get_or_create(name=artist.strip)[0]
        )
    for one_genre in data.getlist('genre')[:3]:
        SongReview(
            song = new_song,
            tag = Tags.objects.get(genre = one_genre),
        ).save()
    return HttpResponse(new_song.song_name)

def average(request, tag):
    tag_list = Song.objects.all(tag)

    num_list = []
    
    avg_num = sum(num_list) / len(num_list)
    return avg_num