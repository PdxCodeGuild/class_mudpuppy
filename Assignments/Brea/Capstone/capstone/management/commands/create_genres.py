from django.core.management.base import BaseCommand
from capstone.models import Genre
import csv

class Command(BaseCommand):
    help = 'Populates the genres database'

    def handle(self, *args, **options):
        with open('capstone/management/commands/genres.csv', encode = encoding='utf-8-sig') as f:
            csv_reader = csv.reader(f, delimiter=',')
            for row in csv_reader:
                Genre.objects.get_or_create(
                    name = row[0],
                )