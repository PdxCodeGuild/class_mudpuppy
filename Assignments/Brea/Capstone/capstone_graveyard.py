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