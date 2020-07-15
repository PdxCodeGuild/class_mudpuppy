from django.core.management.base import BaseCommand
from capstone.models import Quality
import csv

class Command(BaseCommand):
    help = 'Populates the qualities database'

    def handle(self, *args, **options):
        with open('capstone/management/commands/qualities.csv') as f:
            csv_reader = csv.reader(f, delimiter=',')
            for row in csv_reader:
                Quality.objects.get_or_create(
                    name = row[0]
                )