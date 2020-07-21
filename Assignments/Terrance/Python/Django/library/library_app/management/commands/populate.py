from django.core.management.base import BaseCommand, CommandError
from library_app.models import Book, Author
from datetime import datetime
class Command(BaseCommand):
    help = 'Populates the Database'

    def handle(self, *args, **options):
        author1 = Author.objects.get_or_create(last_name='Tolkien', first_name='J', middle1='R.', middle2='R.')[0]
        author2 = Author.objects.get_or_create(last_name='Machado', first_name='Carmen', middle1='Maria')[0]
        books = (
            ('The Lord of the Rings', datetime.strptime('29-07-1954', '%d-%m-%Y'), author1),
            ('The Hobbit', datetime.strptime('21-09-1937', '%d-%m-%Y'), author1),
            ('In the Dream House', datetime.strptime('05-11-2019', '%d-%m-%Y'), author2),
        )
        for one_book in books:
            Book.objects.get_or_create(
                title = one_book[0], 
                publish_date = one_book[1],
                author = one_book[2],
            )
