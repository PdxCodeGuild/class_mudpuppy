from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=128)

class Song(models.Model):
    song_name = models.CharField(max_length=128)
    artist = models.ManyToManyField(Artist)
    release_year = models.IntegerField(null=True, blank=True)
    spotify_link = models.URLField(null=True, blank=True)
    chords_link = models.URLField(null=True, blank=True)
    info_link = models.URLField(null=True, blank=True)

class Tags(models.Model):
    class Modes(models.TextChoices):
        Major = 'MJ', _('Major')
        Minor = 'mn', _('Minor')
        Other = 'Ot', _('Other')

    class Genres(models.TextChoices):
        Blues = 'bls', _('Blues')
        Classical = 'cls', _('Classical/Art')
        Country = 'ctr', _('Country')
        Easy = 'eas', _('Easy Listening')
        Electronic = 'elc', _('Electronic')
        Folk = 'flk', _('Folk')
        Gospel = 'gos', _('Gospel/Soul')
        Hiphop = 'hip', _('Hip-hop/Rap')
        Instrumental = 'ins', _('Instrumental')
        Jazz = 'jzz', _('Jazz')
        Latin = 'ltn', _('Latin')
        Metal = 'mtl', _('Metal')
        Musical = 'brd', _('Musical/Broadway')
        Pop = 'pop', _('General Pop')
        RB = 'r&b', _('Rhythm and Blues')
        Reggae = 'reg', _('Reggae')
        Rock = 'rck', _('Rock')
        World = 'wrl', _('World Music')
        Other = 'oth', _('Other')
        
    genre = models.CharField(
        max_length=20,
        choices=Genres.choices,
        null=True, blank=True,)
    
    mode = models.CharField(
        max_length=5,
        choices=Modes.choices,
        null=True, blank=True,)

    tempo = models.IntegerField(null=True, blank=True)
    singability = models.IntegerField(null=True, blank=True)
    playability = models.IntegerField(null=True, blank=True)
    repetition = models.IntegerField(null=True, blank=True)
    dynamics = models.IntegerField(null=True, blank=True)

    arousal = models.IntegerField(null=True, blank=True)
    popularity = models.IntegerField(null=True, blank=True)
    valence = models.IntegerField(null=True, blank=True)
    emotion = models.CharField(max_length=50,null=True, blank=True)
    theme = models.CharField(max_length=50, null=True, blank=True)
    comments = models.TextField(max_length=500, null=True, blank=True)

class SongReview(models.Model):
    song = models.ForeignKey(Song, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

