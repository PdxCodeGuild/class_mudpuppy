def index(request):
    song_list = Song.objects.all()
    context = {
        'song_list_dict': song_list,
        'choices': Tags.Genres.choices,
    }
    return render(request, 'capstone/index.html', context)



class Artist(models.Model):
    name = models.CharField(max_length=128)

class Song(models.Model):
    song_name = models.CharField(max_length=128)
    artist = models.ManyToManyField(Artist)
    release_year = models.IntegerField(null=True, blank=True)
    
    # spotify_link = models.URLField(null=True, blank=True)
    # chords_link = models.URLField(null=True, blank=True)
    # info_link = models.URLField(null=True, blank=True)

    
    # emotion = models.CharField(max_length=50,null=True, blank=True)
    # theme = models.CharField(max_length=50, null=True, blank=True)

class Comment(models.Model):
    comment = models.TextField(max_length=500, null=True, blank=True)
    song = models.ForeignKey(Song, on_delete = models.PROTECT)
    
class Genre(models.TextChoices):
    # Blues = 'bls', _('Blues')
    # Classical = 'cls', _('W. Classical/Art')
    # Country = 'ctr', _('Country')
    # Easy = 'eas', _('Easy Listening')
    # Electronic = 'elc', _('Electronic')
    # Folk = 'flk', _('Folk')
    # Gospel = 'gos', _('Gospel/Soul')
    # Hiphop = 'hip', _('Hip-hop/Rap')
    # Instrumental = 'ins', _('Instrumental')
    # Jazz = 'jzz', _('Jazz')
    # Latin = 'ltn', _('Latin')
    # Metal = 'mtl', _('Metal')
    # Musical = 'brd', _('Musical/Broadway')
    # Pop = 'pop', _('General Pop')
    # RB = 'r&b', _('Rhythm and Blues')
    # Reggae = 'reg', _('Reggae')
    # Rock = 'rck', _('Rock')
    # World = 'wrl', _('World Traditional')
    # Other = 'oth', _('Other')
    
    genre = models.CharField(
        max_length=20,)

class QualityReview(models.Model):
    song = models.ForeignKey(Song, on_delete=models.PROTECT)
    # user = models.ForeignKey(User, on_delete=models.PROTECT)
    quality = models.ForeignKey('Quality', on_delete=models.PROTECT) #bc we're importing them
    votes = models.IntegerField()

class Quality(models.Model): #captures all 1-7 rating types
    name = models.CharField(max_length=12)
    
    # tempo = models.IntegerField(null=True, blank=True)
    # singability = models.IntegerField(null=True, blank=True)
    # playability = models.IntegerField(null=True, blank=True)
    # repetition = models.IntegerField(null=True, blank=True)
    # # dynamics = models.IntegerField(null=True, blank=True)

    # arousal = models.IntegerField(null=True, blank=True)
    # popularity = models.IntegerField(null=True, blank=True)
    # valence = models.IntegerField(null=True, blank=True)
    
class GenreReview(models.Model):
    song = models.ForeignKey(Song, on_delete=models.PROTECT)
    # user = models.ForeignKey(User, on_delete=models.PROTECT)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    votes = models.IntegerField()

def add_song(request):
    data = request.POST
    print(data)
    new_song = Song(
        song_name = data['song_name'],
        release_year = data['release_year'],

    #     # genre = data['genre'],
    #     tempo = data['tempo'],
    #     singability = data['singability'],
    #     playability = data['playability'],
    #     repetition = data['repetition'],
    #     arousal = data['arousal'],
    #     popularity = data['popularity'],
    #     valence = data['valence'],
    #     comments = data['comment'],
    # )
    artists = data['artist']
    new_song.save()

    new_rev = Review(
        song_id=post_song_id,
        quality_id=post_quality_id,
        score=post_score,
    )
    new_rev.save()

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


from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class Song(models.Model):
    song_name = models.CharField(max_length=100, null=True, blank=True)
    year = models.CharField(max_length=4, null=True, blank=True)
    artist = models.CharField(max_length=50, null=True, blank=True)
    highest_avg = models.ForeignKey('ReviewAvg', on_delete=models.PROTECT, related_name='songs', null=True) # the ForeignKey is the unique id related to a row as created by ReviewAvg, for the genre upvotes

    def __str__(self):
        return self.name

    def reset_highest(self):
        self.highest_avg = max(self.reviews_avgs.all(), key=lambda review: review.score)
        self.save()
        # pulls the highest of all the review averages and saves it as itself

class Quality(models.Model): #captures all 1-7 rating types
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Comment(models.Model):
    comment = models.TextField(max_length=500, null=True, blank=True)
    song = models.ForeignKey(Song, on_delete = models.PROTECT)

class Review(models.Model):
    song = models.ForeignKey(Song, on_delete=models.PROTECT, related_name='reviews')
    quality = models.ForeignKey(Quality, on_delete=models.PROTECT, 
    related_name='reviews_qualityname')
    score = models.IntegerField()
    # creates a Review that intersects the Song and Quality classes, with their given numeric score

class ReviewAvg(models.Model):
    song = models.ForeignKey(Song, on_delete=models.PROTECT, related_name='reviews_avgs')
    quality = models.ForeignKey(Quality, on_delete=models.PROTECT, related_name='reviews_avgs')
    score = models.FloatField()
    count = models.IntegerField()
    # creates a class that averages the numeric scores that intersect between a song and a given quality, while counting how many reviews have been given about that quality

    def add_review(self, review):
        '''Adjust the score and the count based on a review'''
        rev_total = self.score * self.count
        rev_total += review.score
        self.count += 1
        self.score = rev_total / self.count
        self.save()
    
    def reset_average(self):
        '''Totally resets the averages by looking at all reviews'''
        reviews = Review.objects.filter(song=self.song).filter(quality=self.quality)    #pulls all the reviews for a given song on a given quality
        count = len(reviews) #counts how many reviews exist for that intersection
        agg = sum ((review.score for review in reviews))    #adds up all the scores for each review
        self.count = count
        self.score = agg/count  #creates a new average
        self.save()

#MY OLD VIEWS
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
        artists = data['artist'])
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
    # new_rev = Review(
    #     song_id=post_song_id,
        
    #     for pair in review_list:
    #         if pair[1] == 'true':
    #             pair[0]
    # )
    # new_rev.save()

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

     <div class="card-action">
                  <a href="{% url 'capstone:song_display(song.id)' %}">All LoFi Hip-Hop Songs</a>
                </div>
    <div class="card-action">
                  <a href="{% url 'capstone:song_display(song.id)' %}">All Ingrid Michaelson Songs</a>
                </div>
    <a href="#" class="brand-logo">Logo</a>

    <!-- <img class="brand-logo" src="{% static 'capstone/images/A.png' %}" alt="Aoede Logo"> -->