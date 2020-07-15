from django.db import models

class Song(models.Model):
    song_name = models.CharField(max_length=100, null=True, blank=True)
    artist = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.song_name
    
    def avg_review(self):
        reviews = self.reviews  #related name to line 21
        print(reviews)

class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Review(models.Model):
    song = models.ForeignKey(Song, on_delete=models.PROTECT, related_name='reviews')

    tempo = models.IntegerField()

    comment = models.TextField()

    def __str__(self):
        return self.song  + str(tempo)

