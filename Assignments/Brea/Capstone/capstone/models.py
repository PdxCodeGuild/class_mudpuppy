from django.db import models

class Song(models.Model):
    song_name = models.CharField(max_length=100, null=True, blank=True)
    artist = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.song_name
    
    def avg_singability(self):
        reviews = self.reviews.all()  #related name to line 21
        # make a workable average calculation for tempo, hopefully write in a way I can generalize it
        count = 0
        singability_sum = 0
        for review in reviews:
            if review.singability != None:
                singability_sum += review.singability
                count +=1
        singability_avg = round((singability_sum / count), 2)
        return singability_avg

    def avg_playability(self):
        reviews = self.reviews.all()  #related name to line 21
        # make a workable average calculation for tempo, hopefully write in a way I can generalize it
        count = 0
        playability_sum = 0
        for review in reviews:
            if review.playability != None:
                playability_sum += review.playability
                count +=1
        playability_avg = round((playability_sum / count), 2)
        return playability_avg

    def avg_tempo(self):
        reviews = self.reviews.all()  #related name to line 21
        # make a workable average calculation for tempo, hopefully write in a way I can generalize it
        count = 0
        tempo_sum = 0
        for review in reviews:
            if review.tempo != None:
                tempo_sum += review.tempo
                count +=1
        tempo_avg = round((tempo_sum / count), 2)
        return tempo_avg

    def avg_repetition(self):
        reviews = self.reviews.all()  #related name to line 21
        # make a workable average calculation for repetition, hopefully write in a way I can generalize it
        count = 0
        repetition_sum = 0
        for review in reviews:
            if review.repetition != None:
                repetition_sum += review.repetition
                count +=1
        repetition_avg = round((repetition_sum / count), 2)
        return repetition_avg

    def avg_popularity(self):
        reviews = self.reviews.all()  #related name to line 21
        # make a workable average calculation for popularity, hopefully write in a way I can generalize it
        count = 0
        popularity_sum = 0
        for review in reviews:
            if review.popularity != None:
                popularity_sum += review.popularity
                count +=1
        popularity_avg = round((popularity_sum / count), 2)
        return popularity_avg
    
    def avg_arousal(self):
        reviews = self.reviews.all()
        count = 0
        arousal_sum = 0
        for review in reviews:
            if review.arousal != None:
                arousal_sum += review.arousal
                count +=1
        arousal_avg = round((arousal_sum / count), 2)
        return arousal_avg
    
    def avg_valence(self):
        reviews = self.reviews.all()  #related name to line 21
        # make a workable average calculation for valence, hopefully write in a way I can generalize it
        count = 0
        valence_sum = 0
        for review in reviews:
            if review.valence != None:
                valence_sum += review.valence
                count +=1
        valence_avg = round((valence_sum / count), 2)
        return valence_avg
    
    def comment_display(self):
        comments = self.reviews.all()
    
class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Review(models.Model):
    song = models.ForeignKey(Song, on_delete=models.PROTECT, related_name='reviews')
    
    singability = models.IntegerField(null=True, blank=True)
    playability = models.IntegerField(null=True, blank=True)
    repetition = models.IntegerField(null=True, blank=True)
    tempo = models.IntegerField(null=True, blank=True)
    popularity = models.IntegerField(null=True, blank=True)
    arousal = models.IntegerField(null=True, blank=True)
    valence = models.IntegerField(null=True, blank=True)

    comment = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.song.song_name  + ' ' + str(self.tempo)