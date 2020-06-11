[//]: # (
    TODO:
    * Make a separate pipenv file
    * Link to that
    * Advise pipenv use, for windows compatability
)

# Grading Lab with Django/Ajax

## Introduction

The goal of this tutorial is to help you setup a django server that can receive a request and provide a `JSON` response.

## Part 1
### Installing Stuff through PIP

`PIP` lets you install python packages. It stands for "PIP Installs Packages." To use `PIP`, we are going to use are standard command to run python in the terminal. I am going to type this: `py`, but you might have to replace that with `python` or `python3`.

To install Django, we can open up the terminal on Mac or Powershell on Windows and type:

```py -m pip install django```

`-m` means "use a module," which is telling python to use pre-written code that you've already downloaded. `pip` is able to understand the command `install`, and it searches for more code to download that matches the name `django`.

You can see a good example of pip at [w3schools](https://www.w3schools.com/python/python_pip.asp).


We are also going to use a package called `django-cors-headers`, and that will help make our django server more accessable. You can learn more about cors at [mdn](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS).

To install cors headers, we can run:

```py -m pip install django-cors-headers```

## Part 2
### Starting Our Project

In the terminal or Powershell, use `cd` (change directory) to get into a folder that you like. If you want to change directory into `Desktop`, you can type `cd Desktop`. If you want to change directory out of any directory, type `cd ..` to go to the parent directory. You can make sure you are in the right place with `pwd` (print working directory). You can see the files in the directory you are currently in by using `ls` (list) if you are on Mac, and `dir` (directory) if you are on Windows.

When you are in a good place to make a new folder, you can run this command:

```py -m django startproject project```

This should have made a bunch of files and folders for us:

```
project
├── manage.py
└── project
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

The first confusing thing is that it made a folder called `project`, and inside of that folder is another folder called `project`. This can be very confusing.

To make this a little cleaner, let's use the `mv` (move) command, which can move or rename files. We can rename the parent folder to `grading`, and keep the child folder as `project`:

``` mv project grading ```

Now it should look like this:

```
grading
├── manage.py
└── project
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

For this lab, we should only have to edit two files, `settings.py` and `urls.py`. First, we'll tackle `settings.py`, which will be a bunch of configuration.

## Part 3
### Configuring `settings.py`

Let's open the folder with a text editor (for example, vscode). Now we can use our editor to change the files.

I will add comments to make it clear which lines I am changing.

First, we're going to change this section:

```python
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
```

We are going to change `ALLOWED_HOSTS` to allow all incoming connections like this:

```python
DEBUG = True

# ALLOWED_HOSTS = [] # Old line
ALLOWED_HOSTS = ['*'] # New line

# Application definition

INSTALLED_APPS = [
```

Now we are going to add two new lines to allow us to use the `django-cors-headers` package that we downloaded:

```python
INSTALLED_APPS = [             
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders', # New line
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware', # New line
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

Finally, we can add a new line at the bottom to tell the cors package/module to allow traffic from anywhere:

```python
STATIC_URL = '/static/'

CORS_ORIGIN_ALLOW_ALL = True # New Line 
```

Great! We've got that annoying configuring out of the way, let's do the more fun part of editing our `urls.py`.

## Part 4
### Configuring `urls.py`

First, the goal of this is to send back `JSON` to allow an `HTTP` page to communicate with our Django server. `JSON` looks a lot like python, and a lot like javascript. Here is an example of converting python to `JSON`.

```python
>>> import json
>>> json.dumps({'data': ['string', True, None, 10, 1.5]})
'{"data": ["string", true, null, 10, 1.5]}'
```

This part is the python:
```python
{'data': ['string', True, None, 10, 1.5]}
```

This part is the `JSON`, which is often used to communicate over the internet:
```json
'{"data": ["string", true, null, 10, 1.5]}'
```

`JSON` can only send the following information:
* javascript objects
* arrays
* numbers
* strings
* booleans
* null

In order to send `JSON` information, we are going to have to use a django module. We can add an import at the top of `urls.py`:

```python
from django.contrib import admin
from django.urls import path
from django.http import JsonResponse # New line    
```

Now let's add a simple function to test out our server. It will simply tell a movie that we like. You can replace the underscores with an actual movie:

```python
from django.contrib import admin
from django.urls import path
from django.http import JsonResponse           

def movie_fun(request): # New line
    return JsonResponse({'message': 'I like the movie ______'}) # New line
```

The `urlpatterns` variable lets us associate a url path with a function. We can add a line so that users can access our `movie_fun` function.

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', movie_fun), # New line
]         
```

Imagine the domain `google.com` is pointing at your site. Users would be able to go to `google.com/movie/`, and then your function would run, and they would receive a `JSON` response letting them know about a movie you like.

Now we should be able to test out our setup by running the server.

## Part 5
### Running the Server

You will have to use `cd` to get to the folder with `manage.py` in it. If you run `ls` or `dir`, you want to see the folder `project` and the file `manage.py`.

To run your server, you can type:

```
py manage.py runserver
```
It should tell you that the server is running on port 8000.

Now, try opening a browser and typing this into the location bar:
```
127.0.0.1:8000/movie/
```

## Part 6
### Creating the Grading Function

Now we can just add a function after our previous function and before the `urlpatterns`:

```python
def movie_fun(request):
    return JsonResponse({'message': 'I like the movie The Last Airbender'})

def grading_fun(request): # New line
    print(request.GET)
    grade_num = request.GET['grade'] # New line
    grade_num = int(grade_num) # New line
    grade_let = '' # New line
    if grade_num > 90: # New line
        grade_let = 'A' # New line
    elif grade_num > 80: # New line
        grade_let = 'B' # New line
    elif grade_num > 70: # New line
        grade_let = 'C' # New line
    elif grade_num > 60: # New line
        grade_let = 'D' # New line
    else: # New line
        grade_let = 'F' # New line
    return JsonResponse({'grade': grade_let}) # New line

urlpatterns = [
```

And we can add one more thing to our `urlpatterns`:
```python
    return JsonRespone({'grade': grade_let})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', movie_fun),
    path('grading/', grading_fun), # New line
]
```

Now you should get an interesting error if you go to:

```
http://127.0.0.1:8000/grading/
```

It should work if you go to:
```
http://127.0.0.1:8000/grading/?grade=85
```

Your browser should have something like this:
```json
{"grade": "B"}
```

If you look in your terminal where you ran `manage.py`, you should see an output like this:
```
<QueryDict: {'grade': ['85']}>
```

This `QueryDict` is a dictionary created by the query parameters in the url path. If you go to this url:
```
http://127.0.0.1:8000/grading/?grade=85&sky=blue&grass=green
```
Everything to the right of the `&` and separated by the `&`s will be converted into a dictionary, and you should see this output:
```
<QueryDict: {'grade': ['85'], 'sky': ['blue'], 'grass': ['green']}>
```
You can see this output because of a line in our `urls.py`, inside the `grade_fun` function:
```python
print(request.GET)
```
All of the information to the right of the `?` in the url path gets bundled into the `request.GET` dictionary, and we can access that information in our urls.py.

