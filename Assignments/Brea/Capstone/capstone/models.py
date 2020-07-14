from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class Song(models.Model):
    song_name = models.CharField(max_length=100, null=True, blank=True)
    year = models.CharField(max_length=4, null=True, blank=True)
    artist = models.CharField(max_length=32, null=True, blank=True)
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
    song = models.ForeignKey(Song, on_delete=models.PROTECT, related_name='songs')
    quality = models.ForeignKey(Quality, on_delete=models.PROTECT, related_name='songs')
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