from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Song, Genre, Comment, Quality, Review, ReviewAvg #, Mus_Tags, NonMus_Tags

def index(request):
    if request.method == 'POST': # if it's a post request
        #get info out of the request
        post_song_id = int(request.POST['song'])
            #why is the song name in an int field? is it pulling the index according to the related name?
        post_color_id = int(request.POST['quality'])
        post_score = int(request.POST['score'])

        #makes a new review with the post request information per the Review class
        new_rev = Review(
            song_id=post_song_id,
            quality_id=post_quality_id,
            score=post_score,
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

    #If it's a get request
    context = {
        'songs_context': Song.objects.all(),
        'qualities_context': Quality.objects.all(),
        'choices': Genre.objects.all(),
        'scores_context': range(7, 0, -1),
    }
    print( render(
        request,
        'capstone/index.html',
        context
    ).content)
    return render(
        request, 
        'capstone/index.html',
        context
    )