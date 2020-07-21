from django.core.management.base import BaseCommand, CommandError
from wine_tours.models import Vineyard
import csv

class Command(BaseCommand):
        help = 'Makes Vineyards'

        def handle(self, *args, **options):
            with open('vineyards.csv') as f:
                csv_reader = csv.reader(f, delimiter=',', quotechar='"')
                for row in csv_reader:
                    print(row)
                    Vineyard.objects.get_or_create(
                        name=row[0],
                        location=row[1],
                        description=row[2],
                        homepage=row[3],
                                            )