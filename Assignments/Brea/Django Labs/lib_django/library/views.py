from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import Author, Book, Checkout

# Create your views here.
def index(request):
    return render(
        request, 'library/index.html',
        {
            'authors': Author.objects.all(),
        })

def author_detail(request, author_pk):
    author = Author.objects.get(pk=author_pk)
    print(
        [book.title for book in author.book_set.all()]
    )
    return render(
        request,
        'library/detail.html',
        {
            'author': author,
        }
    )

def checkout_page(request, book_pk):
    return render(
        request,
        'library/checkout.html',
        {
            'book': Book.objects.get(pk=book_pk),
        })

def new_checkout(request):
    print("*" * 40)
    print(request.POST)
    active_book = Book.objects.get(pk=request.POST['book_pk'])
    try:
        last_checkout = Checkout.objects.filter(book=active_book).order_by('-timestamp')[0]
    except IndexError:
        last_checkout = None
    checkout_bool = True
    if last_checkout:
        checkout_bool = not last_checkout.checkout
    checkout = Checkout (
        user=request.POST['name'],
        checkout= checkout_bool,
        book=active_book,
    )
    checkout.save()
    return HttpResponseRedirect(reverse('lib:checkout_page', args=[active_book.id]))