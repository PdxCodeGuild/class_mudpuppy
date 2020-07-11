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