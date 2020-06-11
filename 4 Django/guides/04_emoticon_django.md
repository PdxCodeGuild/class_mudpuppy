# Django Emoticon Lab
## Table of contents
1. [Introduction](#introduction)
2. [Setting Up](#setup)
3. [Starting from urls.py](#starting-urls)
4. [Using the Database](#using-database)
5. [Using an HTML Template](#using-template)
6. [Receiving POST Requests](#receiving-post)
## Part 1: Introduction<a name="introduction"></a>

In this walkthrough we are going to have a database of eyes, noses, and mouths, and we are going to make random emoticons from them. The person visiting our site will be able to add their own eyes, noses, and mouths to the database.

## Part 2: Setting Up<a name="setup"></a>
Make a directory called `emoticon_django`, and `cd` into it.

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
py manage.py startapp emo_app
```

Look at the files again, and make sure that you made the directory `emo_app`.

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
    path('emo/', include('emo_app.emo_urls')), # New line
]
```

Now let's pretend that you are hosting this site locally at `http://127.0.0.1:8000`. If you go to your internet browser, and at the top you type `http://127.0.0.1:8000/admin/`, then django will send your request to this `urls.py` file, and it'll parse the url path to deside to send you to the builtin admin site. If you go to `http://127.0.0.1:8000/emo/abc/`, then python will look at the first part of the url path, and it'll decide to send you to a file inside the directory `emo_app` called `emo_urls.py`. Django will send the remaining path, `abc/` to that file for processing. We don't have a `emo_urls.py` yet, so we'll have to make one.

```emo_app/emo_urls.py
from django.urls import path, include
from . import views

urlpatterns = [
       path('', views.index)
]
```
This file is checking if there's nothing left after the initial `emo/` in the url path, and as long as that's true it's sending the user to the `index` function inside the `views.py` file. That file doesn't have that function in it, so let's add that function into `views.py`.

```python
from django.shortcuts import render
from django.http import HttpResponse # New line
from random import choice # New line

def index(request): # New line
       return HttpResponse( # New line
               choice(';:') + # New line
               choice('>-') + # New line
               choice(')]') # New line
       ) # New line
```

Now, in your pipenv environment, make sure that you are in the same directory as `manage.py`, and then run:

```
py manage.py runserver
```

Now you should be able to go to [http://127.0.0.1:8000/emo/](http://127.0.0.1:8000/emo/) and see a random emoticon.

## Part 4: Using the Database<a name="using-database"></a>

Whenever you want to use the database, you first need to modify the `models.py` file inside an app folder, and then you have to tell django to sync up the database with that file.

First, let's modify the `models.py` file:

```python
from django.db import models

class Eye(models.Model): # New line
       char = models.CharField(max_length=1) # New line

       def __str__(self): # New line
               return self.char # New line

class Nose(models.Model): # New line
       char = models.CharField(max_length=1) # New line

       def __str__(self): # New line
               return self.char # New line

class Mouth(models.Model): # New line
       char = models.CharField(max_length=1) # New line

       def __str__(self): # New line
               return self.char # New line
```

These classes will all become database tables. You can imagine a separate area in an Excel sheet for Eye, Nose, and Mouth. Each area would have two columns: `id` and `char`. `id` is automatically added in django, so that everything in the database has a unique numerical id number (databases generally need something unique).

We also tell our models what they should look like when someone tries to convert them to a string. For example,

```python
>>> from emo_app.models import Eye
>>> one_eye = Eye(char="B")
>>> str(one_eye)
'B'
```

Whenever you try to convert an eye, a nose, or a mouth into a string, each will run their `__str__` method, and will return their character.

We could make our code more concise using a mixin, but we're not going to worry about that for now.

Because we are using the database, we need to tell django that our app, `emo_app`, is an installed app. We can do that in the `settings.py` file.

```python
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'emo_app', # New line
]
```

Now we can update the database. Start by using `Ctrl-C` to kill the server. Then use `ls` or `dir` to make sure that you are in the same directory as your `manage.py` file. If you cannot see the `manage.py` file, use `cd` to change to another directory.

Now run the following commands:

```
py manage.py makemigrations
py manage.py migrate
```

This should tell you that, because of the changes made to `models.py`, django is restructuring the database.

We can now use the python shell to add info into our database. Run this command:

```
py manage.py shell
```

And inside python shell, you can run these commands:

```python
>>> from emo_app.models import Eye, Nose, Mouth
>>> new_eye = Eye(char=":")
>>> new_eye.save()
>>> new_eye = Eye(char=";")
>>> new_eye.save()
>>> new_nose = Nose(char="-")
>>> new_nose.save()
>>> new_mouth = Mouth(char=")")
>>> new_mouth.save()
>>> quit()
```
Now I would recommend downloading [sqlitebrowser](https://sqlitebrowser.org/dl/) and opening up the db.sqlite3 file to see your data.

## Part 5: Using an HTML Template<a name="using-template"></a>

We can modify our `views.py` file to use emoticon information from our database, instead of hardcoded strings:
```python
from django.shortcuts import render
from django.http import HttpResponseRedirect # Changed line
from random import choice
from .models import Eye, Nose, Mouth # New line

def index(request):
       # return HttpResponse( # Deleted line
       #         choice(';:') + # Deleted line
       #         choice('>-') + # Deleted line
       #         choice(')]') # Deleted line
       # ) # Deleted line
       eyes = list(Eye.objects.all())
       noses = list(Nose.objects.all())
       mouths = list(Mouth.objects.all())
       emoticon = str(choice(eyes)) + str(choice(noses)) + str(choice(mouths))
       context = {'emoticon_template_var': emoticon}
       return render(request, 'emo_app/index.html', context)
```

Index will get a list of all eyes in the database, all noses in the database, and all mouths in the database. It will randomly choose from one of each, and convert them into strings. Context will be a dictionary, and when django looks at the html file it will replace `emoticon_template_var` with our emoticon.

On that last line we added, we are telling `render` to look for a file `emo_app/index.html`. We haven't made this file yet. The file structure might be confusing, because the file will actually be in `emo_app/templates/emo_app/index.html`.

Make the directories `templates` and `emo_app`, and then make the file `index.html`:
```html
<!DOCTYPE html>
<html>
       <head>
               <meta charset="utf-8">
       </head>
       <body>
               <h1>{{emoticon_template_var}}</h1>
       </body>
</html>
```

`emoticon_template_var` will be replaced by our emoticon.

Now we should be able to run the server and go to the site and see an emoticon with a random set of eyes. We could see more randomness if we added more stuff to the database. But why don't we let the person visiting the website add to the database?

## Part 6: Receiving POST Requests<a name="receiving-post"></a>

First, we need to add to our `index.html` file:
```html
       <body>
               <h1>{{emoticon}}</h1>
               <form method="POST" action="add/"> # New line
                       {% csrf_token %} # New line
                       <input type="text" placeholder=":" name="new"> # New line
                       <input type="hidden" name="type" value="eye"> # New line
                       <button>submit</button> # New line
               </form> # New line
               <form method="POST" action="add/"> # New line
                       {% csrf_token %} # New line
                       <input type="text" placeholder="-" name="new"> # New line
                       <input type="hidden" name="type" value="nose"> # New line
                       <button>submit</button> # New line
               </form> # New line
               <form method="POST" action="add/"> # New line
                       {% csrf_token %} # New line
                       <input type="text" placeholder=")" name="new"> # New line
                       <input type="hidden" name="type" value="mouth"> # New line
                       <button>submit</button> # New line
               </form> # New line
       </body>
```
Each form section is ready to send it's own information to `/emo/add/`. We should make sure that we will be able to catch it. Because the method is "POST" instead of "GET", we can send information in this http request. You can visualize this information as a dictionary, with the keys as the name attributes of input elements, and the values as the values of those input elements.

`{% csrf_token %}` is a secret password that gets embedded into your html page. You can view it by opening up the site in a browser and inspecting the source html.

Pretend that you click on the first text input box, and you type "B", and click the button. A POST request will be sent to `emo/add/`. You can imagine a dictionary inside this POST request that looks like this:

```python
{
		'csrfmiddlewaretoken': 'qtqkOy1uTubxV0iwfFEqqeCu0nR4JhEgP7Zafu16Wa2gdsJoDm8Za6KAHB7KRYhS',
		'type': 'eye',
		'new': 'B',
}
```

Change `emo_app/emo_urls.py` like this:
```python
urlpatterns = [
       path('', views.index),
       path('add/', views.add), # New line
]
```

This is directing the `add/` part of the url path to go to a function in `views.py` called `add`, but that function doesn't exist yet. Let's add it now. Add this after the index function:

```python
def add(request):
	   print('dictionary:'.ljust(15), request.POST)
	   print('raw:'.ljust(15), request.body)
       data = request.POST
       face_parts = {
                       'eye': Eye,
                       'nose': Nose,
                       'mouth': Mouth,
       }
       new_part_class = face_parts[data['type']]
       new_part = new_part_class(char=data['new'])
       new_part.save()
       return HttpResponseRedirect('/emo/')
```
You should be able to add to the database by adding a character and pushing the button. Because we just added the lines of code in the `add` function that prints out info from the request, we can see the raw request and the request structured in a dictionary. It should appear where we ran `py manage.py runserver`.

Based on what the hidden input fields in the forms said, we will know if the user wanted to add an eye, nose, or mouth. We can use that information to decide if we want to use the Eye, Nose, or Mouth class from our `models.py`. We can create one of those using the character that the user sent, and then we can save what we created in our database.

Then we redirect the user back to the page. It is bad to leave the user on a post request, because everytime they hit refresh it will re-send the information.

Great job!

## Part 7: Refactoring<a name="receiving-post"></a>

Not Yet Written
