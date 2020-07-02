# populate.py 
# Automatically populates my database for testing

from django.core.management.base import BaseCommand, CommandError
from capstone.models import Song

class Command(BaseCommand):
    help = 'Populates the Database'

    def handle(self, *args, **options):
        song1 = Song.objects.get_or_create(song_name="", artist_name="", release_year="", spotify_link="", chords_link="", info_link="")
        song2 = Song.objects.get_or_create(song_name="", artist_name="", release_year="", spotify_link="", chords_link="", info_link="")
        song3 = Song.objects.get_or_create(song_name="", artist_name="", release_year="", spotify_link="", chords_link="", info_link="")
        song4 = Song.objects.get_or_create(song_name="", artist_name="", release_year="", spotify_link="", chords_link="", info_link="")
        song5 = Song.objects.get_or_create(song_name="", artist_name="", release_year="", spotify_link="", chords_link="", info_link="")
        song6 = Song.objects.get_or_create(song_name="", artist_name="", release_year="", spotify_link="", chords_link="", info_link="")
        song7 = Song.objects.get_or_create(song_name="", artist_name="", release_year="", spotify_link="", chords_link="", info_link="")