from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Song, Genre, Comment, Quality, Review, ReviewAvg #, Mus_Tags, NonMus_Tags

#make function that adds the immutable song information
#make a new html input page for the first time a song added
def index(request):
    #this is giving me the landing page
    #If it's a get request 
    context = {
        'songs_context': Song.objects.all(),
        'qualities_context': Quality.objects.all(),
        'choices': Genre.objects.all(),
        'scores_context': range(7, 0, -1),
    }
    # print( render(
    #     request,
    #     'capstone/index.html',
    #     context
    # ).content)
    return render(
        request, 
        'capstone/index.html',
        context
    )

def add_review(request):
    data = request.POST
    print(data)
    new_song = Song(
        song_name = data['song_name'],
        release_year = data['release_year'],
        artists = data['artist']
    new_song.save()

    #get info out of the request
    post_song_id = new_song.id
    #make a bunch of variables for each slider quality
    

    post_singability = int(request.POST['singability'])
    post_singability2 = request.POST['singability2']

    post_playbility = int(request.POST['playbility'])
    post_playbility2 = request.POST['playbility2']

    post_repetition = int(request.POST['repetition'])
    post_repetition2 = request.POST['repetition2']

    post_tempo = int(request.POST['tempo'])
    post_tempo2 = request.POST['tempo2']

    post_popularity = int(request.POST['popularity'])
    post_popularity2 = request.POST['popularity2']

    post_arousal = int(request.POST['arousal'])
    post_arousal2 = request.POST['arousal2']

    post_valence = int(request.POST['valence'])
    post_valence2 = request.POST['valence2']

    review_list = [
        (post_singability, post_singability2),
        (post_playbility, post_playability2),
        (post_repetition, post_repetition2),
        (post_tempo, post_tempo2),
        (post_popularity, post_popularity2),
        (post_arousal, post_arousal2),
        (post_valence, post_valence2),
    ]

    #makes a new review with the post request information per the Review class
    new_rev = Review(
        song_id=post_song_id,
        
        for pair in review_list:
            if pair[1] == 'true':
                pair[0]
    )
    new_rev.save()

    #try to update the review average for that song and quality
    try:    #if the song and a given quality rating exist, integrate the new review for those two items into the existing data
        rev_avg = ReviewAvg.objects.get(
            song_id = post_song_id,
            quality_id = post_quality_id,
        )
        rev_avg.add_review(new_rev)

    except ObjectDoesNotExist: #or, add this as the first information for this song and that given quality if it does not yet exist
        ReviewAvg(
            song_id=post_song_id,
            quality_id=post_quality_id,
            score=post_score,
            count=1
        ).save()

    song = Song.objects.get(pk=post_song_id)
    song.reset_highest()

    return HttpResponseRedirect('/index/') #eventually, I want them to go to the song display page for the song they just reviewed