# Django Links Example
## Table of contents
1. [Introduction](#introduction)
2. [Setting Up](#setup)
3. [Starting from urls.py](#starting-urls)
4. [Using the Database](#using-database)
5. [Creating a Custom Command](#custom-command)
6. [Setting up the Views](#setting-views)
7. [Real Comments](#real-comments)

## Part 1: Introduction<a name="introduction"></a>

In this walkthrough we are going to have a database of links that can be shown on the front page. We can also see and make comments for each link. The first three parts look similar to the previous guide.

## Part 2: Setting Up<a name="setup"></a>
Make a directory called `links_django`, and `cd` into it.

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
py manage.py startapp links_app
```

Look at the files again, and make sure that you made the directory `links_app`.

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
    path('links/', include('links_app.links_urls')), # New line
]
```

Now let's pretend that you are hosting this site locally at `http://127.0.0.1:8000`. If you go to your internet browser, and at the top you type `http://127.0.0.1:8000/admin/`, then django will send your request to this `urls.py` file, and it'll parse the url path to deside to send you to the builtin admin site. If you go to `http://127.0.0.1:8000/links/abc/`, then python will look at the first part of the url path, and it'll decide to send you to a file inside the directory `links_app` called `links_urls.py`. Django will send the remaining path, `abc/` to that file for processing. We don't have a `links_urls.py` yet, so we'll have to make one.

```python
from django.urls import path, include
from . import views

urlpatterns = [
       path('', views.index),
]
```
This file is checking if there's nothing left after the initial `links/` in the url path, and as long as that's true it's sending the user to the `index` function inside the `views.py` file. That file doesn't have that function in it, so let's add that function into `views.py`.

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

Now you should be able to go to [http://127.0.0.1:8000/links/](http://127.0.0.1:8000/links/) and see "hello".

## Part 4: Using the Database<a name="using-database"></a>

Whenever you want to use the database, you first need to modify the `models.py` file inside an app folder, and then you have to tell django to sync up the database with that file.

First, let's modify the `models.py` file:

```python
from django.db import models

class Link(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, unique=True)
    link = models.CharField(max_length=128)

    def __str__(self):
        return self.slug[:10]

    def __repr__(self):
        return self.slug[:10]
```

We will have one table in our database for the Link model. The name and the link are a bunch of characters to keep in the database. The slug is also characters, but formatted to work in a URL.

```python
>>> article_name = "Stuff and Things: A Meta Conversation"
>>> from django.utils.text import slugify
>>> slugify(article_name)
'stuff-and-things-a-meta-conversation'
```

Next time you go to a news site, check to see if you can see a slug in the url path. For example, [https://www.djangoproject.com/weblog/2020/apr/29/pycharm-dsf-campaign-2020-results/](https://www.djangoproject.com/weblog/2020/apr/29/pycharm-dsf-campaign-2020-results/). The term `slug` means a short title, which comes from news media. In our models.py, we gave the SlugField the keyword argument `unique=True`, because we don't want two links to have the same slug.

We are also giving our Link class a `__str__` method, so that someone can convert it to a string, and we are giving it a `__repr__` method. The `__repr__` method means "How an instance represents itself." An easy way to think of `__repr__` is this: if there is a Link inside of a list or dictionary, what should it look like? Feel free to change `__repr__` to return something you'll notice, like `🎉`. Python's good with unicode.

Now we need to update `settings.py`.

```python
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'links_app', # New line
]
```

Now we can update the database. Start by using `Ctrl-C` to kill the server. Then use `ls` or `dir` to make sure that you are in the same directory as your `manage.py` file. If you cannot see the `manage.py` file, use `cd` to change to another directory.

Now run the following commands:

```
py manage.py makemigrations
py manage.py migrate
```

This should tell you that, because of the changes made to `models.py`, django is restructuring the database.


## Part 5: Creating a Custom Command<a name="custom-command"></a>

Let's put some stuff in our database. I don't always like using `py manage.py shell` to put stuff in there. If we set up a custom command, which will take lots of work, we can be a little bit lazy in the future (it won't be worth it).

First, we need to create our directories to make our file. Our directory structure should look like this: `links_app/management/commands/`. Make the directory `management`, and then inside of that make the directory `commands`. Once you've done that, you can make a file called `make_links.py`.

Now, we'll copy the basic structure of a command. Here's what `make_links.py` should start as (this part doesn't have to make as much sense):

```python
from django.core.management.base import BaseCommand

class Command(BaseCommand):
       help = ''

       def handle(self, *args, **options):
			pass
```

Now we can add some stuff that should make more sense:

```python
from django.core.management.base import BaseCommand
from links_app.models import Link # New line
from django.utils.text import slugify # New line

class Command(BaseCommand):
       help = 'Adding some links to the database' # Changed line

       def handle(self, *args, **options):
               # pass  # Deleted line
               for pairing in ( # New line
                               ('good search site', 'google.com'), # New line
                               ('good reviews', 'avclub.com'), # New line
                               ): # New line
                               Link.objects.get_or_create( # New line
                                       name=pairing[0], # New line
                                       slug=slugify(pairing[0]), # New line
                                       link=pairing[1] # New line
                               ) # New line
```
Now when someone runs our custom command, we can use a tuple for `google.com` and a tuple for `avclub.com`, and we can use them to create new instances of the Link class from our `models.py` file. `get_or_create` will either find that information in the database, or if it can't find that information then it will create it. This means that you can run the custom command multiple times, and it won't create multiple rows in the database with the same information.


We should be able to see our custom command by running:

```
py manage.py help
```

It should output something like this:

```
[links_app]
    make_links
```

That's the file we made, inside of the app we made! Now we can run:


```
py manage.py make_links
```

Now this will add our links into the database. You can check the database using [sqlitebrowser](https://sqlitebrowser.org/dl/).

## Part 6: Setting up the Views<a name="setting-views"></a>


This is your views.py:
```python
from django.shortcuts import render
from .models import Link

def index(request):
       all_links = Link.objects.all()
       context = {
               'all_links_template': all_links,
       }
       return render(request, 'links_app/index.html', context)

def link_slug(request, in_slug):
       found_link = Link.objects.get(slug=in_slug)
       comments = ['its great', 'its bad']
       context = {
               'found_link_template': found_link,
               'comments_template': comments,
       }
       return render(request, 'links_app/slug.html', context)
```

The first function searches for all links in the database, and renders an html template with all the links. It'll hand off our google link and our avclub link to the `index.html` file (which we haven't written yet). Inside that file, we'll probably write a for loop and loop over all the instances of our Link class, and through that we can put info from the database into our html file.

The second function takes a new parameter, `in_slug`. We will see how to pass information to this function. It gets the link associated with the slug, and it passes that link and some comments to the `slug.html` file.


Now let's add to the `links_urls.py` file:

```python
app_name = "links_paths" # New line
urlpatterns = [
    path('list/', views.index, name="index_path"), # Changed line
    path('l/<str:in_slug>/', views.link_slug, name="slug_path"), # New line
]
```
(People often get errors in this file because they forget to put a comma at the end of every line).

On that new line, we are telling django that there will be a variable in the url path. The `<str:in_slug>` is telling django to look for a string there, and then pass it to the `views.link_slug` function as the parameter `in_slug`. If we look at the first line of that function in `views.py`, `def link_slug(request, in_slug):`, we can see where django will receive that info. The slug part of the url will be used to look up the right link in the database. For example, if you go to `http://127.0.0.1:8000/links/s/good-search-site/, django will receive an http request and send the string `good-search-site` to the `link_slug` function. Then, in that function we are using that string to look up the proper link. Keep in mind that in `models.py` we used this line: `slug = models.SlugField(max_length=128, unique=True)`. We set unique to true, meaning that only one row in our database can have each slug. So each string we can put in will either give us no rows from our database (and an error), or it will give us one row.

Now let's setup some html files. First we need to make the directories `links_app/templates/links_app`, and then we need to make two html files in there.

index.html:

```html
<!DOCTYPE html>
<html>
       <head>
               <meta charset="utf-8">
               <style>
                       .link-holder {
                                       border: 4px solid black;
                                       margin: 50px;
                                       padding: 20px;
                       }

               </style>
       </head>
       <body>
               {% for link in all_links_template %}
                       <div class="link-holder">
                               <h2><a href="https://{{link.link}}">{{link.name}}</a></h2>
                               <h4><a href="{% url 'links_paths:slug_path' in_slug=link.slug %}">comments</a></h4>
                       </div>
               {% endfor %}
       </body>
</html>
```

slug.html:

```html
<!DOCTYPE html>
<html>
       <head>
               <meta charset="utf-8">
               <style>
                       .comment-div {
                               border: 2px solid black;
                               background-color: lemonchiffon;
                               margin: 20px;
                               padding: 5px;
                       }
                       .comment-div:hover {
                               border: 2px solid blue;
                               background-color: coral;
                       }
               </style>
       </head>
       <body>
               <h1><a href="https://{{found_link_template.link}}">{{found_link_template.name}}</a></h1>
               <h4>Comments</h4>
               {% for comment in comments_template %}
               <div class="comment-div">
                       {{ comment }}
               </div>
               {% endfor %}
       </body>
</html>
```

Whenever you see `{{}}` or `{%%}`, that usually means that it's accessing info from the context dictionary. For reference, the context dictionary in `views.py` in the `get_slug` function, which uses the `slug.html` template, is this:

```python
       found_link = Link.objects.get(slug=in_slug)
       comments = ['its great', 'its bad']
       context = {
               'found_link_template': found_link,
               'comments_template': comments,
       }
```

So inside the `slug.html` file, when it says `{% for comment in comments_template %}`, it's looping over that list from `views.py`, `comments = ['its great', 'its bad']`. Information passes through that context dictionary, and then django does an advanced find-and-replace to replace all the keys in the context dictionary ('found_link_template', 'comments_template') with the values.

Now, try running the server and checking out the site.

Check out the main site, and try inspecting the html. Inside the `index.html` file, we had this:

```html
       <body>
               {% for link in all_links_template %}
                       <div class="link-holder">
                               <h2><a href="https://{{link.link}}">{{link.name}}</a></h2>
                               <h4><a href="{% url 'links_paths:slug_path' in_slug=link.slug %}">comments</a></h4>
                       </div>
               {% endfor %}
       </body>
```
If we look at the html that the browser sees, we should see the for-loop expanded in the html. We should also see the two `<a>` tags with actual links in them. The first link is from information in the database. The second link is generated from getting path information from `links_urls.py`, and passing in a link's slug, which will be used to look up info from our database.

Now let's set up some real comments (though we're not doing user authentication, so maybe not *real* comments).

## Part 7: Real Comments<a name="real-comments"></a>

First, let's add to our `models.py`. Put this new class on the bottom:

```python
class Comment(models.Model):
       link = models.ForeignKey(Link, on_delete=models.CASCADE)
       text = models.TextField()
```
TextField can take some big text. The database has no max limit for this field.

`link` is a foreign key to the `Link` class. Imagine the `Link` table looks like this:

`Link`
| ID             | Name         | Link         | Slug         |
| :------------: | :----------: | :----------: | :----------: |
| 1              | search site  | google.com   | search-site  |
| 2              | review site  | avclub.com   | review-site  |

Now if you have two comments that are associated with the google.com link, then your `Comment` table might look like this:

`Comment`
| ID             | Link         | Text                   |
| :------------: | :----------: | :--------------------: |
| 1              | 1            | This site is awesome   |
| 2              | 1            | This site is awful     |

Both links are `1` because they are associated with the row in the `Link` table that has an ID of `1`.

What would happen if we deleted that row 1 in the `Link` table? The first thing to remember is that IDs cannot be reused, so no other site can have an ID of 1.

We would have two comments that refer to a link that does not exist. Because in our `models.py` we said `on_delete=models.CASCADE`, we would delete the two comments that have a foreign key to that link.

Now we can add to our custom command since we have to populate our comments as well. We can add this to the bottom:

```python
                               Link.objects.get_or_create(
                                       name=pairing[0],
                                       slug=slugify(pairing[0]),
                                       link=pairing[1]
                               )

               google_link = Link.objects.get(link="google.com") # New line
               for text in ('I love this site!', 'I hate this site!'): # New line
                               Comment.objects.get_or_create( # New line
                                       text=text, # New line
                                       link_id=google_link.id, # New line
                                       ) # New line
```

And we can add an import to the top:

```python
from django.core.management.base import BaseCommand
from links_app.models import Link, Comment # Changed line
from django.utils.text import slugify
```

Here we are grabbing our google link, and creating two comments that are associated with that link.


Now we can change our `views.py`, since we actually have real comments:
```python
from django.shortcuts import render
from .models import Link, Comment # Changed line
```

```python
       comments = found_link.comment_set.all() # Changed line
       context = {
               'found_link': found_link,
```

This is saying to get all the comments pointing at our link we found. In the table example above, it would be like if we had the `google.com` link with an id of `1`, and then asking for every comment that has a foreign key with a value of `1`.

And we can add a new function to the bottom of `views.py`:

```python
def add_comment(request):
       data = request.POST
       new_comment = Comment(
               link_id = data['link'],
               text = data['commenttext'],
       )
       new_comment.save()
       link_slug = Link.objects.get(id=data['link']).slug
       return HttpResponseRedirect(reverse('links_paths:slug_path', args=[link_slug]))
```

Also, add some imports:
```python
from django.shortcuts import render, reverse # Changed line
from django.http import HttpResponseRedirect # New line
from .models import Link, Comment
```


Here we are receiving a POST request and parsing the data. We can inject the relavent link's ID into the request, so that we know what link the user was looking at when they made the comment. If they were looking at the `google.com` link with an ID of `1`, we want to associate their comment with that link, and not the link to `avclub.com`.

We can put the info into our database by creating and saving an instance of our `Comment` class. Then we can create the url from info in our `links_urls.py` and the slug associated with the link the user was looking at, and redirect their browser back to that link. They should see their page refresh and their comment appear on the page, but otherwise they shouldn't see any consequence.

Now let's add one more path to our `links_urls.py`:
```python
urlpatterns = [
    path('list/', views.index, name="index_path",),
    path('s/<str:in_slug>/', views.link_slug, name="slug_path",),
    path('comment/', views.add_comment, name="comment_path",), # New line
]
```

And add to our `slug.html`:
```html
               {% for comment in comments_template %}
               <div class="comment-div">
                       {{ comment.text }} # Changed line
               </div>
               {% endfor %}
               <form method="POST" action="{% url 'links_paths:comment_path' %}"> # New line
                       {% csrf_token %} # New line
                       <input type="hidden" name="link" value="{{found_link_template.id}}"></input> # New line
                       <textarea placeholder="Type your comment here" name="commenttext"></textarea> # New line
                       <button>submit</button> # New line
               <form> # New line
        </body>
 </html>
```

Now we have a small form which can send the id of the link that we are looking at, and the text of the comment, which are the two things that we need to add a new comment to our database.

Test it out and make sure it works!
