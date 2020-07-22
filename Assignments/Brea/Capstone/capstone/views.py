from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Song, Genre, Review

def index(request):
    context = {
        'songs_context': Song.objects.all(),
        'choices': Genre.objects.all(),
    }
    return render(
        request,
        'capstone/index.html',
        context
    )

def add_review(request):
    data = request.POST
    print(data)

    new_song_input, created = Song.objects.get_or_create(
        song_name = data['song_name'],
        artist = data['artist'],
    )

    if created == True:
        new_song_input.save()

    new_review = Review(
        song = new_song_input,
        singability = int(data['singability']),
        playability = int(data['playability']),
        repetition = int(data['repetition']),
        tempo = int(data['tempo']),
        popularity = int(data['popularity']),
        arousal = int(data['arousal']),
        valence = int(data['valence']),
        # genre = data['genre'],
        comment = data['comment'],
    )
    new_review.save()

    for genre_id in data.getlist('genre'): 
        new_review.genre.add(int(genre_id))
    return HttpResponseRedirect(reverse('capstone:song_display', kwargs={'song_id': new_song_input.id}))

def song_display(request, song_id):
    context = {
        'song': Song.objects.get(id=song_id),
        # 'review': Review.objects.get(id=)
    }
    # print(context['song'].genre_display())

    return render (
        request,
        'capstone/song_display.html',
        context,
    )

def artist_display(request, artist):
    context = {
        'artist': Song.objects.all().filter(artist),
    }

    return render (
        request,
        'capstone/artist_display.html',
        context,
    )

def song_browse(request):
    context = {
        'song': Song.objects.all(),
        'Britney': Song.objects.filter(artist = 'Britney Spears'),
        'Ingrid' : Song.objects.filter(artist = 'Ingrid Michaelson'),
        'Disney': Song.objects.filter(artist = 'Disney'),
        'LoFi': Song.objects.filter(artist = 'LoFi'),
        'Sia': Song.objects.filter(artist = 'Sia'),
        'Regina': Song.objects.filter(artist = 'Regina Spektor'),
    }

    return render (
        request,
        'capstone/song_browse.html',
        context,
    )

def landing(request):
    context = {
        'data': Song.objects.all(),
        'Ingrid' : Song.objects.filter(artist = 'Ingrid Michaelson'),
        'LoFi' : Song.objects.filter(artist = 'LoFi'),
    }

    return render(
        request,
        'capstone/landing_page.html',
        context,
    )