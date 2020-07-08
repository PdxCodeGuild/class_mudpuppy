# Django User Notes Example
## Table of contents
1. [Introduction](#introduction)
2. [Setting Up](#setup)
3. [Starting from urls.py](#starting-urls)
4. [Making a Second App](#second-app)
5. [Using the Database](#using-database)
6. [Making a Details Page](#making-details)
6. [Making the Checkout](#making-checkout)

## Part 1: Introduction<a name="introduction"></a>

This is a walkthrough to make a page that allows the user to have notes, complete with user registration and user login.

## Part 2: Setting Up<a name="setup"></a>
Make a directory called `notes_django`, and `cd` into it.

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
py manage.py startapp notes
```

Look at the files again, and make sure that you made the directory `notes`.

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
    path('notes/', include('notes.notes_urls')), # New line
]
```

Now let's pretend that you are hosting this site locally at `http://127.0.0.1:8000`. If you go to your internet browser, and at the top you type `http://127.0.0.1:8000/admin/`, then django will send your request to this `urls.py` file, and it'll parse the url path to deside to send you to the builtin admin site. If you go to `http://127.0.0.1:8000/notes/abc/`, then python will look at the first part of the url path, and it'll decide to send you to a file inside the directory `notes` called `notes_urls.py`. Django will send the remaining path, `abc/` to that file for processing.

Now, let's make the file `notes/notes_urls.py`

```python
from django.urls import path, include
from . import views

urlpatterns = [
       path('', views.index),
]
```
This file is checking if there's nothing left after the initial `notes/` in the url path, and as long as that's true it's sending the user to the `index` function inside the `views.py` file. That file doesn't have that function in it, so let's add that function into `views.py`.

```python
from django.shortcuts import render
from django.http import HttpResponse # New line

def index(request): # New line
       return HttpResponse('notes go here') # New line
```

Now, in your pipenv environment, make sure that you are in the same directory as `manage.py`, and then run:

```
py manage.py runserver
```

Now you should be able to go to [http://127.0.0.1:8000/notes/](http://127.0.0.1:8000/notes/) and see "notes go here".


## Part 4: Adding Login Requirement<a name="adding-login-requirement"></a>

First, let's try adding a login required decorator to our function in `notes/views.py`:

```python
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required # New line

@login_required # New line
def index(request):
       return HttpResponse('notes go here')
```

Now, if we try to go to [http://127.0.0.1:8000/notes/](http://127.0.0.1:8000/notes/), django will notice that you are not logged in, and try to send you to this url: <http://localhost:8000/accounts/login/?next=/notes/>. Django is trying to send you to the default url for login, which is `/accounts/login/` and it is trying to remember that you want to go to `/notes/` once you succesfully login by adding the query parameter `next=/notes/`. Unfortunately, this default login url doesn't lead anywhere, so we will get an error.

To better understand default login, let's add another function to our `notes/views.py` file:


```python
@login_required
def index(request):
       return HttpResponse('hi')

def best_food(request): # New line
       return HttpResponse('pizza') # New line
```

And now we can add another line to our `project/settings.py` file:

```python
USE_TZ = True
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
LOGIN_URL = '/notes/best_food/' # New line
```

And another path in our `notes/notes_urls.py` file:

```python
urlpatterns = [
       path('', views.index),
       path('best_food/', views.best_food), # New line
]
```

Now if we try to go to 


Now, if we try to go to <http://127.0.0.1:8000/notes/>, it should see that we are not logged in, and then send us to the `LOGIN_URL` set inside the `project/settings.py` file, which is `/notes/best_food/`.

Eventually we will create our own page to login and register users, but for now let's use the django built-in login and registration.

First, we need to construct our database so that django can save user information. Let's run these commands:

```
py manage.py makemigrations
py manage.py migrate
py manage.py createsuperuser
```

Now we can go to <http://127.0.0.1:8000/admin/>, which should redirect us to the admin login page, and then we can login with the superuser we just created.

Now, without logging out, go back to <http://127.0.0.1:8000/notes/>, and you should successfully see the page `notes go here`. If you want to logout, you have to go back to <http://127.0.0.1:8000/admin/>, and from there you should see a logout button.


## Part 5: Adding Login Page<a name="adding-login-page"></a>

First, let's create a `users` app to handle login and logout:

```
py manage.py startapp users
```

Now, let's edit our `project/urls.py` file to include our new user urls file:

```python
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('notes/', include('notes.notes_urls')),
    path('users/', include('users.users_urls')), # New line
]
```

This means we need to make a file, `users/users_urls.py`. Let's make that file and put this inside of it:

```python
from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
       path('login-page/', views.login_page, name='login_page'),
]
```

This file is importing views and using the function `views.login_page`, so let's edit `users/views.py` and add that function:


```python
from django.shortcuts import render

def login_page(request):
       data = request.GET # Ref 1
       context = {
                       'next': data.get('next', '/notes/'), # Ref 2
               }
       return render(
                       request,
                       'users/login_page.html',
                       context
                       )
```

`Ref 1` is grabbing all the query parameters out of the url path. So, before when django created the url `http://localhost:8000/accounts/login/?next=/notes/`, django would package that `next=/notes/` into a dictionary-type thing that's similar to this:
```python
	{
		'next': '/notes/',
	}
```

`Ref 2` will try to get the value associated with the key `next`, and if that doesn't exist then it will give the default, `/notes/`.

`users/login_page.html` refers to a template that doesn't exist, so let's create that template. We have to create two directories: inside of `users` we have to make a directory called `templates`, and inside that we have to make another directory called `users`, and inside of that directory we can make the file `login_page.html`. So it should be `users/templates/users/login_page.html`. Inside `login_page.html`, put the following:

```html
       <h1>Login</h1>
       <form action="" method="POST">
               {% csrf_token %}
               <input type="hidden" name="next" value="{{next}}">
               <input type="text" name="username" placeholder="username">
               <input type="password" name="password" placeholder="password">
               <button type="submit">Login</button>
       </form>
```

Here, we say `name="next" value="{{next}}"` so that we can grab the next url path from the context dictionary in our `views.py` file, and then send that back when this form sends out information.

Now let's make a couple of additions to the `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'notes', # New line
    'users', # New line
]
```

Those will tell django to look at the `models.py` files and the `templates` folders inside of our app folders, `notes/` and `users/`.

And let's change the `LOGIN_URL` in `settings.py`:

```python
USE_TZ = True
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
LOGIN_URL = 'users:login_page' # Changed line
```

Now, if we are not logged in, then django should send us to our (incomplete) login page. Test it out, by logging out at `/admin/` and then going to `/notes/`.


## Part 6: Adding Login<a name="adding-login"></a>

We have are login page, but we can't actually login. Let's change that.

First, let's add stuff to our `users/views.py`. We need a bunch of imports first:

```python
from django.shortcuts import render, reverse # Changed line
from django.http import HttpResponseRedirect # New line
from django.contrib.auth import login, logout, authenticate # New line
from django.contrib.auth.models import User # New line
```

And we need to add three new functions at the bottom:

```python
                       context
                       )

def login_view(request): # New line
    username = request.POST['username'] # New line
    password = request.POST['password'] # New line
    user = authenticate(request, username=username, password=password) # New line
    login(request, user) # New line
    return HttpResponseRedirect(request.POST['next']) # New line

def logout_view(request): # New line
    logout(request) # New line
    return HttpResponseRedirect(reverse('users:login_page')) # New line

def register(request): # New line
    username = request.POST['username'] # New line
    email = request.POST['email'] # New line
    password = request.POST['password'] # New line
    new_user = User.objects.create_user(username, email, password) # New line
    login(request, new_user) # New line
    return HttpResponseRedirect('/notes/') # New line
```

And since we added three functions to `views.py`, we need to add three more paths to `users_urls.py`:

```python
urlpatterns = [
       path('login-page/', views.login_page, name='login_page'),
       path('register/', views.register, name='register'), # New line
       path('login/', views.login_view, name='login'), # New line
       path('logout/', views.logout_view, name='logout'), # New line
]
```

And we need to add a bunch of stuff into `users/templates/users/login_page.html` to allow registration:

```html
       <h1>Register</h1> # New line
       <form action="{% url 'users:register' %}" method="POST"> # New line
               {% csrf_token %} # New line
               <input type="hidden" name="next" value="{{next}}"> # New line
               <input type="text" name="username" placeholder="username"> # New line
               <input type="text" name="email" placeholder="email"> # New line
               <input type="password" name="password" placeholder="password"> # New line
               <button type="submit">Register</button> # New line
       </form> # New line
       <h1>Login</h1>
       <form action="{% url 'users:login' %}" method="POST"> # Changed line
               {% csrf_token %}
               <input type="hidden" name="next" value="{{next}}">
               <input type="text" name="username" placeholder="username">

```

And now we should be able to register new users or login an existing user at `/users/login-page/`.

We can quickly add a logout link to our `notes/views.py` by changing one line:

```python
@login_required
def index(request):
       return HttpResponse('notes<br><a href="/users/logout">logout</a>') # Changed line

def best_food(request):
       return HttpResponse('pizza')
```

Now, when you go to `/note/` there should be a logout button.


## Part 7: Saving a User's Notes<a name="saving-users-notes"></a>

We never actually modified our `models.py` in either of our apps. The `users` app is going to use the builtin users, and a bunch of builtin django user management stuff, so we don't need to worry about that one. We should edit the `notes/models.py` and add these:

```
from django.db import models
from django.contrib.auth.models import User # New line

class Note(models.Model): # New line
    text = models.CharField(max_length=128) # New line
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes') # New line
```

After we create this file, we need to makemigrations and migrate again:

```
py manage.py makemigrations
py manage.py migrate
```

And let's create a real `index` function in our `notes/views.py`:
```python
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import lo
in_required
from .models import Note # New line
import random # New line

note_list = ['I like movies', 'I like music'] # New line # Ref 1
@login_required
def index(request):
       return HttpResponse('notes<br><a href="/users/logout">logout</a>') # Deleted line
       Note( # New line # Ref 2
                       user=request.user, # New line # Ref 3
                       text = random.choice(note_list) # New line # Ref 4
                       ).save() # New line # Ref 5
       output = '' # New line
       active_user = request.user # New line # Ref 6
       print(active_user.username) # New line # Ref 7
       notes_associated_with_user = active_user.notes.all() # New line # Ref 8
       print([note.text for note in notes_associated_with_user]) # New line # Ref 9
       for note in notes_associated_with_user: # New line
               output = output + note.text + '<br>' # New line # Ref 10
       output = output + '<a href="/users/logout/">logout</a>' # New line # Ref 11
       return HttpResponse(output) # New line
```

I added the comment `# Ref` to allow us to reference different lines:

1. `Ref 1` is a list of two options for notes text. We could let the user send us what they want us to put into the notes text, but in order to be concise we are just going to randomly pick the notes text from two options.

2. We are using the `Note` class that we imported from the `notes/models.py` file. We should think about this class as representing a row in our database. We are creating a new note, so we are creating a new row in our database.

3. The new row in the database will refer to the user who is currently logged in, which we can access through `request.user`.

4. The new row in the database will have a random note text from our note list. A full site would allow the user to send this information to us, but for this small example our notes will randomly have the text `I like movies` or `I like books`.

5. This will save the new row to the database.

6. This is getting the user currently using the page.

7. This is printing out the current user's username. You should be able to see your username printed out where you ran `py manage.py runserver`.

8. `active_user.notes.all()` grabs every note associated with the currently logged in user.

9. This will print out the text of every note associated with the current user. You should be able to see this where you ran `py manage.py runserver`.

10. This adds the text of every note associated with the user.

11. This adds a logout link.


Now you should be able to login/logout, register, and refreshing the `/notes/` page wil add a new note for the user. Different users have their own notes, that persist after logging out and logging back in.
