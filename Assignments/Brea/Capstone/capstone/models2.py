from django.db import models

class Song(models.Model):
    song_name = models.Charfield(max_length=100, null=True, blank=True)
    artist = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Review(models.Model):
    song = models.ForeignKey(Song, on_delete=models.PROTECT, related_name='reviews')

    tempo = models.IntegerField()

class ReviewAvg(models.Model):
    song = models.ForeignKey(Song, on_delete=models.PROTECT, related_name='reviews_avg')
    tempo = models.ForeignKey(Review, on_delete=models.PROTECT, related_name='reviews_avg')
    score = models.FloatField()
    count = models.IntegerField()

    def add_review(self, review):
        '''Adjust the score and count with a new quality review'''
        rev_total = self.tempo * self.count
        rev_total += review.tempo 
        self.count += 1
        self.score = rev_total / self.count
        self.save()

    def reset_avg(self):
        '''Totally resets the average by looking at all available scores for a quality'''
        reviews = Review.objects.filger(song=self.song).filter(quality=self.tempo)
        count = len(reviews)
        agg = sum
