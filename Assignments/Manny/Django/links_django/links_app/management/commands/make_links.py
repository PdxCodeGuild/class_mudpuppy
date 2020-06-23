from django.core.management.base import BaseCommand
from links_app.models import Link
from django.utils.text import slugify 

class Command(BaseCommand):
        help = ''
        #print("Hello")
        def handle(self, *args, **options):
			#pass 
            for pairing in ( # New line
                               ('good search site', 'google.com'), # New line
                               ('good reviews', 'avclub.com'), # New line
                               ): # New line
                               Link.objects.get_or_create( # New line
                                       name=pairing[0], # New line
                                       slug=slugify(pairing[0]), # New line
                                       link=pairing[1] # New line
                               ) # New line

