# Django Library Walkthrough
## Table of contents
1. [Introduction](#introduction)
2. [Setting Up](#setup)
3. [Starting from urls.py](#starting-urls)
4. [Making a Second App](#second-app)
5. [Using the Database](#using-database)
6. [Making a Details Page](#making-details)
6. [Making the Checkout](#making-checkout)

## Part 1: Introduction<a name="introduction"></a>

This is a walkthrough to complete [django lab 4](../labs/lab04-library.md)

## Part 2: Setting Up<a name="setup"></a>
Make a directory called `lib_django`, and `cd` into it.

Run the following commands:

```
py -m pipenv install
py -m pipenv install django
py -m pipenv shell
```

Now you should be in your virtual environment.

You can start your project by running:

```
py -m django startproject project .
```

That last `.` represents the directory that you are in. For example, if you want to see how much space the current directory is using, you can use
```
du -h .
```

If you type `ls -1` on mac or `dir` on windows, you should see the following:

```
manage.py
Pipfile
Pipfile.lock
project
```

You can also look at these files in a file explorer, and they should look the same.

Now we are going to create an app. This app should help us keep functions in a specific folder associated with a purpose. It will also help us connect python functions with the ORM (object-relational mapper), which allows us to use python objects to interact with the database.

We can create our app with this command:
```
py manage.py startapp library
```

Look at the files again, and make sure that you made the directory `library`.

## Part 3: Starting from urls.py<a name="starting-urls"></a>
Now it is helpful to think about incoming requests, and the structure of django. You create a request everytime you tell your browser to go to a website. You say, "I request this website's information." Incoming requests will come through `project/wsgi.py` (Web Server Gateway Interface). Inside `wsgi.py` this line:

```python
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
```
Tells your system to look to the file `project/settings.py` to get settings info.

Inside of `settings.py` there is a line that looks like this:

```python
ROOT_URLCONF = 'project.urls'
```

This tells django to send initial http requests to the project.urls file. Let's look at that file. Starting out, it should look like this:

```python
"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```
This file gives us a lot of advice. We are going to follow the advice here:
> Including another URLconf
>    1. Import the include() function: from django.urls import include, path
>    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

So we will change the file in the following way:
```python
from django.contrib import admin
from django.urls import path, include # Changed line

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lib/', include('library.lib_urls')), # New line
]
```

Now let's pretend that you are hosting this site locally at `http://127.0.0.1:8000`. If you go to your internet browser, and at the top you type `http://127.0.0.1:8000/admin/`, then django will send your request to this `urls.py` file, and it'll parse the url path to deside to send you to the builtin admin site. If you go to `http://127.0.0.1:8000/lib/abc/`, then python will look at the first part of the url path, and it'll decide to send you to a file inside the directory `library` called `lib_urls.py`. Django will send the remaining path, `abc/` to that file for processing.

Now, let's make the file `library/lib_urls.py`

```python
from django.urls import path, include
from . import views

urlpatterns = [
       path('', views.index),
]
```
This file is checking if there's nothing left after the initial `lib/` in the url path, and as long as that's true it's sending the user to the `index` function inside the `views.py` file. That file doesn't have that function in it, so let's add that function into `views.py`.

```python
from django.shortcuts import render
from django.http import HttpResponse # New line

def index(request): # New line
       return HttpResponse('hello') # New line
```

Now, in your pipenv environment, make sure that you are in the same directory as `manage.py`, and then run:

```
py manage.py runserver
```

Now you should be able to go to [http://127.0.0.1:8000/lib/](http://127.0.0.1:8000/lib/) and see "hello".

## Part 4: Making a Second App<a name="second-app"></a>

This part is unnecessary for creating the library project, but it's a good learning exercise.

Let's make an app called `calc`. Our goal can be to make a simple calculator that can add and subtract numbers. We can make it by running:

`py manage.py startapp calc`

And now we should see the calc folder.

The next step is to modify the `project/urls.py`, because that is the root `urls` that points at the app `urls` files.

from django.contrib import admin
from django.urls import path, include

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('lib/', include('library.lib_urls')),
    path('calc/', include('calc.calc_urls')), # New line
]
```

Again, that `calc.calc_urls` points at a file that doesn't exist. We need to create the file `calc/calc_urls.py`:

```python
from django.urls import path
from . import views
urlpatterns = [
    path('add/<int:num1>/<int:num2>/', views.add),
    path('sub/<int:num1>/<int:num2>/', views.sub),
]
```

We have not setup the `views.py` yet, but with the current setup the user can go to /calc/add/100/10/, and then django will look for a function `add` inside of `views.py` and try to hand them the numbers `100` and `10`.

At the top, it says `from . import views`. This means, "from the current directory import `views.py`." This is good, because we don't want to use `/library/views.py`, we want to use `/calc/views.py`. This file will import the correct `views.py` file.

Now, let's add to the `views.py` so that it looks like this:

```python
from django.shortcuts import render
from django.http import HttpResponse

base = '''
<body style="height:100vh;width:100vw;background-color:lemonchiffon">
<h1>{type} Results</h1>
<h3>{results}</h3>
</body>
'''

def add(request, num1, num2):
    return HttpResponse(
        base.format(
            type='Addition',
            results=num1+num2,
        )
    )

def sub(request, num1, num2):
    return HttpResponse(
        base.format(
            type='Subtraction',
            results=num1-num2,
        )
    )
```

Now, if we run the server, the following links should work:

[http://127.0.0.1:8000/calc/add/100/10/](http://127.0.0.1:8000/calc/add/100/10/)

[http://127.0.0.1:8000/calc/sub/100/10/](http://127.0.0.1:8000/calc/sub/100/10/)

Now that these work, we don't ever have to use the calculator again. This example was to illustrate the difference between the path /lib/ and /calc/, which you can think of as taking you to different app folders.

```
├── calc
│   ├── admin.py
│   ├── apps.py
│   ├── calc_urls.py # if your path starts with /calc/
│   ├── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── library
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── lib_urls.py # if your path starts with /lib/
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
├── Pipfile
├── Pipfile.lock
├── project
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py #main urls, sends you to other urls.py files
│   └── wsgi.py
```

For the rest of this guide, we will edit stuff in `library/`, and will not edit stuff in `calc/`. It's tricky because both have a `views.py`, `models.py`, and `urls.py` (though we gave the `urls.py`s different names).

## Part 5: Using the Database<a name="using-database"></a>

Now let's put stuff into our `models.py`:

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=128)
    publish_date = models.DateField()
    author = models.ForeignKey('Author', on_delete=models.PROTECT)

class Author(models.Model):
    last_name = models.CharField(max_length=32)
    first_name = models.CharField(max_length=32)
    middle1 = models.CharField(max_length=16, blank=True, null=True)
    middle2 = models.CharField(max_length=16, blank=True, null=True)
```

Whenever we modify the models.\_\_\_\_Field methods in the models.py file, we need to run `makemigrations` and `migrate`. They might not work this time, though.

First, we can try:

```
py manage.py makemigrations
```

and 

```
py manage.py migrate
```

It should do a lot, but it doesn't create tables based on our `models.py` file. This is because we never installed our app into Django. You can install it by editing the `settings.py` file in our project folder:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'library', # New line
]
```

Now let's try running `makemigrations` again. Now it should automagically create a new file in our `/library/migrations/` folder. That file is based off of our `models.py` file.

Next, we can try `migrate` again. Now it should use the files inside of `/library/migrations/` to modify our `db.sqlite3` file.

We can create a custom command to populate the database. It's always better to have a database with some data in it, even if that data is fake. It will help us understand how our site is functioning. Make the directories `library/management/commands/`, and then inside of that make a file called `populate.py`. Our folder should look like this:

```
├── calc
│   ├── admin.py
│   ├── apps.py
│   ├── calc_urls.py
│   ├── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── library
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── lib_urls.py
│   ├── management
│   │   └── commands
│   │       └── populate.py # Here's our new file
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
├── Pipfile
├── Pipfile.lock
├── project
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
```

And here's what `populate.py` will look like:

```python
from django.core.management.base import BaseCommand, CommandError
from library.models import Book, Author
from datetime import datetime
class Command(BaseCommand):
       help = 'Populates the Database'

       def handle(self, *args, **options):
               author1 = Author.objects.get_or_create(last_name='Tolkien', first_name='J.', middle1='R.', middle2='R.')[0]
               author2 = Author.objects.get_or_create(last_name='Machado', first_name='Carmen', middle1='Maria')[0]
               books = (
                       ('The Lord of the Rings', datetime.strptime('29-07-1954', '%d-%m-%Y'), author1),
                       ('The Hobbit', datetime.strptime('21-09-1937', '%d-%m-%Y'), author1),
                       ('In The Dream House', datetime.strptime('05-11-2019', '%d-%m-%Y'), author2),
               )
               for one_book in books:
                               Book.objects.get_or_create(
                                       title = one_book[0],
                                       publish_date = one_book[1],
                                       author = one_book[2],
                               )
```

Now we should be able to run our custom command and have two authors and three books in our database. Try running it like this:

```
py manage.py populate
```


Now, let's try to see some of this info inside of our website.

First, we can modify our `views.py` so that it looks like this:

```python
from django.shortcuts import render
from .models import Author

def index(request):
       return render(
               request,
               'library/index.html',
               {
                       'authors': Author.objects.all(),
       })
```

This only works if we have an `index.html` file, which we do not yet have. Let's make it. First we need to make the directories `library/templates/library/` and then we can put the `index.html` file in there.

```

├── calc
│   ├── admin.py
│   ├── apps.py
│   ├── calc_urls.py
│   ├── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── library
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── lib_urls.py
│   ├── management
│   │   └── commands
│   │       └── populate.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── templates
│   │   └── library
│   │       └── index.html # New file
│   ├── tests.py
│   └── views.py
├── manage.py
├── Pipfile
├── Pipfile.lock
├── project
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
```

That `index.html` file should look like this:

```html
<!DOCTYPE html>
<html>
       <head>
               <meta charset="utf-8">
       </head>
       <body>
               <h1>Authors</h1>
               <ul>
               {% for author in authors %}
                       <li>{{ author.last_name }}</li>
               {% endfor%}
               </ul>
       </body>
</html>
```

Now we should be able to run our server, and it will show a list of authors from our database.

It would be cool if we could have the names look better, though. First, let's modify our `models.py`:

```python
       first_name = models.CharField(max_length=32)
       middle1 = models.CharField(max_length=16, blank=True, null=True)
       middle2 = models.CharField(max_length=16, blank=True, null=True)

       def name_formatted(self): # New line
               output = f"{self.last_name}, {self.first_name}" # New line
               if self.middle1: # New line
                               output += f" {self.middle1}" # New line
                               if self.middle2: # New line
                                               output += f" {self.middle2}" # New line
               return output # New line
```

Now we have a method that can give a formatted representation of the name. Because we didn't touch any of the `Field`s, we do not need to run `makemigrations` or `migrate` for this change. Now let's change our `index.html` To use this method:

```html
               <ul>
               {% for author in authors %}
                       <li>{{ author.name_formatted }}</li> # Changed line
               {% endfor%}
               </ul>
```

Now we should be able to see the author's names displayed nicely.



## Part 6: Making the Details<a name="making-details"></a>

First, let's add an `author_detail` function to our `views.py` file. You should change an import at the top:

```
from .models import Book, Author # Changed line
```

And then you'll add a new function at the bottom of the file:

```python
def author_detail(request, author_pk): # New line
       author = Author.objects.get(pk=author_pk) # New line
       print( # New line
               [book.title for book in author.book_set.all()] # New line
       ) # New line
       return render( # New line
               request, # New line
               'library/detail.html', # New line
               { # New line
                       'author': author, # New line
       }) # New line
```

This function takes in a `pk`, which stands for `primary key`, which is the same thing to Django as an `id`. Generally, a primary key in a database is a column that is unique, that each row can be identified by. Django automatically makes the primary key a number that increments everytime you save something new to the database.

This function references an html file, `library/detail.html`. Let's create that.

```html
<!DOCTYPE html>
<html>
       <head>
               <meta charset="utf-8">
       </head>
       <body>
               <h1>{{ author.name_formatted }}</h1>
               <ul>
               {% for book in author.book_set.all %}
                       <li>{{ book.title }} -- {{ book.publish_date }}</li>
               {% endfor%}
               </ul>
       </body>
</html>
```

This syntax, `author.book_set.all`, can be quite confusing. We will look at that in a bit.

Now we need to add to our `lib_urls.py` to include this `author_detail` function.

```python
from django.urls import path
from . import views

app_name = 'lib' # New line
urlpatterns = [
       path('', views.index),
       path('auth/<int:author_pk>/', views.author_detail, name="author_detail"), # New line
]
```

When we say `app_name =` and `path(name=`, those will allow us to give a nickname to a url path, and then we can have django automatically fill in the url paths. Sometimes we do that in our html files, and sometimes we do that in our `views.py` file.

Also, keep in mind that that syntax, `path('auth/<int:author_pk>/', views.author_detail,`, means that part of the url path will be handed to the `views.author_detail` function. If we go to `/lib/auth/2/`, then the number `2` will be handed to that function, and the function in our `views.py` will run like this:

```python
def author_detail(request, author_pk): # author_pk = 2
       author = Author.objects.get(pk=author_pk) # author at 2nd row of database
```

Now we just need our `index.html` to link to the author detail pages. We can change it like this:

```html
               <ul>
               {% for author in authors %}
                       <li><a href={% url 'lib:author_detail' author.id %}>{{ author.name_formatted }}</a></li> # Changed line
               {% endfor%}
               </ul>
```

Now, we should be able to run our server and see a list of links to author detail pages.

When we do check the author detail page, let's look at the printout. In our `views.py` file, under the `author_detail` function, we print this out: 
```python
       print(
               [book.title for book in author.book_set.all()]
       )
```

The last part, `author.book_set.all()`, is getting every book associated with an author. This is a list comprehension, so it's basically a for-loop. The list is going to have the `book.title` for every book that's associated with that author.

Keep in mind that authors and books are connected by a foreign key, which looks kind of like this:

`Author`
| id (pk)        | last\_name   | first\_name  |
| :------------: | :----------: | :----------: |
| 1              | Austen       | Jane         |
| 2              | Tolkein      | J.           |

Now if you have two comments that are associated with the google.com link, then your `Comment` table might look like this:

`Book`
| id (pk)        | author\_id   | title                  |
| :------------: | :----------: | :--------------------: |
| 1              | 1            | Sense and Sensibility  |
| 2              | 1            | Emma                   |


So if we get the author Jane Austen, and then we say `author.book_set.all()`, that is getting every `Book` that has an `author_id` value of 1.

Inside of our `details.html` template, we also use `{% for book in author.book_set.all %}`. This is how we can refer to all the rows in our database that refer to another row in our database, and have it appear in our html file.

## Part 7: Making the Checkout<a name="making-checkout"></a>

First, we can add a new model at the bottom of our `models.py` file:

```python
class Checkout(models.Model):
       book = models.ForeignKey('Book', on_delete=models.PROTECT)
       user = models.CharField(max_length=32)
       checkout = models.BooleanField()
       timestamp = models.DateTimeField(auto_now_add=True)
```

Now, every checkout will point at a book through a foreign key. It will record the user checking in or checking out the book. It will remember if it's true that it's a checkout, or if it's false that it's a checkout (meaning that it's a book return). And it will remember when the record was created.

We will have to `makemigrations` and `migrate` again.

Now we can add stuff to our `views.py` file. Start by changing the imports at the top:

```python
from django.shortcuts import render, reverse # Changed line
from .models import Book, Author, Checkout # Changed line
from django.http import HttpResponseRedirect # New line

def index(request):
```

And we can add two new functions at the bottom:

```python
def checkout_page(request, book_pk): # New line
       return render( # New line
               request, # New line
               'library/checkout.html', # New line
               { # New line
                       'book': Book.objects.get(pk=book_pk), # New line
       }) # New line
```

The `checkout_page` fuction is quite similar to the other functions. It uses the template `library/checkout.html`, which does not exist yet. Let's create that.

Here is `library/checkout.html`:

```html
<!DOCTYPE html>
<html>
       <head>
               <meta charset="utf-8">
       </head>
       <body>
               <h1>{{ book.title }}</h1>
               <h3>Checkout or return</h3>
               <form method="POST" action="{% url 'lib:new_checkout'%}">
                       {% csrf_token %}
                       <input type='hidden' name='book_pk' value='{{book.pk}}'>
                       <input type='text' placeholder='name' name='name'>
                       <button type='submit'>submit</button>
               </form>
               <ul>
               {% for checkout in book.checkout_set.all %}
                       <li>
                       {{ checkout.timestamp }}
                       {% if checkout.checkout %}
                               checked out
                       {% else %}
                               returned
                       {% endif %}
                       by {{ checkout.user }}
                       </li>
               {% endfor %}
               </ul>
       </body>
</html>
```

In this template, once again we loop over a `_set.all`, which means "loop over every checkout associated with this book."

Before that, we have a form, which will try to send information to a path that doesn't exist. When we say `<form method="POST" action="{% url 'lib:new_checkout'%}">`, Django will try to inject a url path like this: `action="/path/here/"`. When Django paress the `'lib:new_checkout'`, it will understand the `lib` part, because in our `lib_urls.py` we say `app_name = 'lib'`. It will not find a path with `name='new_checkout'` because we haven't made that yet.

Between the `<form>` and the `</form>` we can see everything that we are sending to our server through a `POST` request. If our `views.py` receives this request, then it should have access to a dictionary, `request.POST`. This dictionary will be based on the inputs between `<form>` and `</form>`. It should be similar to this, but it won't be exactly this:
```python
{
	'csrf_password': 'secretpassword_abc123',
	'name': 'Charlie Brown',
	'book_pk': '4',
}
```

This is assuming that `Charlie Brown` typed their name into the website to checkout the book that is on the 4th row of our database.

Now we can add to our `lib_urls.py`:

```python
       path('auth/<int:author_pk>/', views.author_detail, name="author_detail"),
       path('checkout/<int:book_pk>/', views.checkout_page, name="checkout_page"), # New line
       path('newcheck/', views.new_checkout, name="new_checkout"), # New line
]
```

And we can imports to our `views.py` file:

```python
from django.shortcuts import render, reverse # Changed line
from .models import Author, Book, Checkout # Changed line
from django.http import HttpResponseRedirect # New line
```

And we can add a new function to the bottom:

```python
               'library/checkout.html',
               {
                       'book': Book.objects.get(pk=book_pk),
       })

def new_checkout(request): # New line
       print(request.POST) # New line
       active_book = Book.objects.get(pk=request.POST['book_pk']) # New line
       try: # New line
               last_checkout = Checkout.objects.filter(book=active_book).order_by('-timestamp')[0] # New line
       except IndexError: # New line
               last_checkout = None # New line
       checkout_bool = True # New line
       if last_checkout: # New line
               checkout_bool = not last_checkout.checkout # New line
       checkout = Checkout( # New line
               user=request.POST['name'], # New line
               checkout = checkout_bool, # New line
               book=active_book, # New line
       ) # New line
       checkout.save() # New line
       return HttpResponseRedirect(reverse('lib:checkout_page', args=[active_book.id])) # New line
```

The `new_checkout` function does a lot. Instead of accessing it through a `get` request, we will access it through a `post` request, meaning that we can pull out a lot of info. The line `print(request.POST)` should let us see that dictionary that gets created from information between the `<form>` tags. You can see we are pulling info from the user's input where we type `request.POST['name']`. We can also pull info from the hidden input where we injected the book's pk. That's an easy way to always know what book we are talking about.

This bit of code is worth looking at:
```python
01       try:
02               last_checkout = Checkout.objects.filter(book=active_book).order_by('-timestamp')[0]
03       except IndexError:
04               last_checkout = None
05       checkout_bool = True
06       if last_checkout:
07                       checkout_bool = not last_checkout.checkout
```

In order for this site to function properly, we must toggle between checking out and returning. To know whether we are checking out or returning, we need to know the most recent Checkout, because that can tell us if the book was just checked out or returned.

On line `02` we will get all of the Checkouts that are associated with the book you are referencing, and it will order them from least recent to most recent. By getting index zero, we can get the most recent Checkout. However, if there are no relavent Checkouts, then there is no index zero, and we will get an `IndexError`.

On lines `01` and `03`, we insure that we are prepared for an `IndexError`. If there are no Checkouts, then line `04` will run, setting `last_checkout` to `None`, and since `None` is seen as similar to `False`, line `07` will not run.

If it is not the first Checkout associated with a book, then line `07` will run. This will save a boolean that's the opposite of the saved boolean. For example, if the most recent row in our database has a `False` value in the `checkout` column, then we are setting our variable `checkout_bool` to `not False`, which is `True`. This is how we accomplish our toggle.

It would be nice if we could get to the `checkout` page from the `author_detail` page, so now let's change our `detail.html` file:

```html
                <h1>{{ author.name_formatted }}</h1>
                <ul>
                {% for book in author.book_set.all %}
                       <li><a href="{% url 'lib:checkout_page' book.pk %}">{{ book.title }} -- {{ book.publish_date }}</a></li> # Changed line
                {% endfor%}
                </ul>
        </body>
```

Now we should be able to access it.

Now, try running the server. Everything should be working great!
