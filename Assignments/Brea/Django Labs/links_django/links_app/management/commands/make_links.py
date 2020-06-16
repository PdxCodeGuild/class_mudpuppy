from django.core.management.base import BaseCommand
from links_app.models import Link, Comment
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Adding some links to the database'

    def handle(self, *args, **options):
        for pairing in (
            ('good search site', 'google.com'),
            ('good reviews', 'avclub.com'),
            ):
            Link.objects.get_or_create(
                name=pairing[0],
                slug=slugify(pairing[0]),
                link=pairing[1],
            )

        google_link = Link.objects.get(link="google.com")
        for text in ('I love this site!', 'I hate this site!'):
            Comment.objects.get_or_create(
                text=text,
                link_id=google_link.id,
            )