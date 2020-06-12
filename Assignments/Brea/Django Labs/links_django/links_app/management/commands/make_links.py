from django.core.managementbase import BaseCommand
from links_app.models import Link
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Adding some links to the database'

    def handle(self, *args, **options):
        for pairing in (
            ('good search site', 'googlecom'),
            ('good reviews', 'avclub.com'),
            ):
            Link.objects.get_or_create(
                name=pairing[0],
                slug-slugify(pairing[0]),
                link=pairing[1],
            )