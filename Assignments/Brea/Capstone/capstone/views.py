from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Song, Genre, Review

def index(request):
    context = {
        'songs_context': Song.objects.all(),
    }
    return render(
        request,
        'capstone/index.html',
        context
    )

def add_review(request):
    data = request.POST

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
        comment = data['comment'],
    )
    new_review.save()

    # average_tempo = new_song_input.avg_review()
    # print(new_song_input.reviews.all())
    return HttpResponse('It worked!')

# def average_score(request, song_id):
#     Review.objects.filter(song_id)
#     return pass

def song_display(request, song_id):
    context = {
        'song': Song.objects.get(id=song_id),
        # 'review': Review.objects.get(id=)
    }
    return render (
        request,
        'capstone/song_display.html',
        context,
    )

