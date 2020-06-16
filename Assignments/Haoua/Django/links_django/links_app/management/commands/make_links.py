from django.core.management.base import BaseCommand
from links_app.models import Link # New line
from django.utils.text import slugify # New line

class Command(BaseCommand):
    help = 'Adding some links to the database' # Changed line

    def handle(self, *args, **options):
               # pass  # Deleted line
        for pairing in (
            ('good search site', 'google.com'), # New line
            ('good reviews', 'avclub.com'), # New line
        ): # New line
            Link.objects.get_or_create(
                name=pairing[0], # New line
                slug=slugify(pairing[0]), # New line
                link=pairing[1] # New line
            ) # New line