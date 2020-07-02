from django.db import models

# Create your models here.
class Song(models.Model):
    song_name = models.CharField(max_length=128)
    artist_name = models.CharField(max_length=128)
    release_year = models.IntegerField(null=True)
    spotify_link = models.URLField(null=True)
    chords_link = models.URLField(null=True)
    info_link = models.URLField(null=True)

    # song_tags = models.ManyToManyField()

# class Mus_Tags(models.Model):
#     mode_choices = [
#         (Major, 'Major'),
#         (Minor, 'Minor'),
#         (Other, 'Other')
#     ]
#     genre = models.Charfield(max_length=50)
#     tempo = models.IntegerField()
#     singability = models.IntegerField()
#     harmonic_comp = models.IntegerField()
#     repetition = model.IntegerField()
#     mode = models.CharField(max_length=5, choices=mode_choices)

# class NonMus_Tags(models.Model):
#     mention_choices = [
#         (Drugs, 'Drugs'),
#         (Sex, 'Sex'),
#         (Self-Harm, 'Self-Harm'),
#         (Other, 'Other')
#     ]
#     arousal = models.IntegerField()
#     # emotions = pass
#     # age_category = pass
#     mentions = models.CharField(max_length=10, choices=mention_choices)
#     cultural_info = models.TextField()
#     interventions_ideas = models.TextField()


