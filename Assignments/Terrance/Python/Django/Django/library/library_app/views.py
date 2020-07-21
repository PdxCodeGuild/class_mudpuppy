from django.shortcuts import render, reverse
from .models import Author, Book, Checkout
from django.http import HttpResponseRedirect

def checkout_page(request, book_pk):
    return render(
        request, 
        'library/checkout.html',
        {
            'book':Book.objects.get(pk=book_pk),
        })

def index(request):
    return render(
        request,
        'library/index.html',
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
        })
        
def new_checkout(request):
    print(request.POST)
    active_book = Book.objects.get(pk=request.POST['book_pk'])
    try: 
        last_checkout = Checkout.objects.filter(book=active_book).order_by('-timestamp')[0]
    except IndexError:
        last_checkout = None
    checkout_bool = True
    if last_checkout:
        checkout_bool = not last_checkout.checkout
    checkout = Checkout(
        user=request.POST['name'],
        checkout = checkout_bool,
        book=active_book,
    )
    checkout.save()
    return HttpResponseRedirect(reverse('lib:checkout_page', args=[active_book.id]))



# from django.http import HttpResponse

# base = '''
# <body style="height:100vh;width:100vw;background-color:lemonchiffon'>
# <h1>{type} Results </h1>
# <h3>{results}</h3>
# </body>
# '''
# def add(request, num1, num2):
#     return HttpResponse(
#         base.format(
#             type='Addition',
#             results=num1+num2,
#         )
#     )
# def sub(request, num1, num2):
#     return HttpResponse(
#         base.format(
#             type='Subtraction',
#             results=num1-num2,
#         )
#     )

# def index(request):
#     return HttpResponse('hello')


# Create your views here.
