from django.core.management.base import BaseCommand
from horoscope_app.models import Sign
import csv
from datetime import datetime
from django.utils.timezone import make_aware



class Command(BaseCommand):
    
    def handle(self, *args, **options):
        with open("Zodiac Signs.csv") as f:
            csv_reader = csv.reader(f,delimiter=',' )
            for row in csv_reader:
                lower = datetime.strptime(row[1]+'-UTC', "%Y-%m-%d-%Z")
                lower.replace = make_aware(lower.replace)
                upper = datetime.strptime(row[2]+'-UTC', "%Y-%m-%d-%Z")
                upper.replace = make_aware(upper.replace)
                Sign.objects.get_or_create(
                    sign = row[0],
                    lower_date = lower,
                    upper_date = upper,
                )
            