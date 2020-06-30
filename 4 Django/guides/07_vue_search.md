# Django Filter Example with Vue
## Table of contents
1. [Introduction](#introduction)
2. [Setting Up](#setup)
3. [Our first JSON Response](#json-response)
4. [Getting a List of Animals](#list-animals)
5. [Adding Vuejs](#adding-vue)
6. [Adding a Lifecycle Hook](#adding-hook)
7. [Adding a Search Function](#search-function)

## Part 1: Introduction<a name="introduction"></a>

Our goal is to filter a list from an input box with vuejs and django.

## Part 2: Setting Up<a name="setup"></a>
Make a directory called `vue_filter`, and `cd` into it.

Run the following commands:

```
py -m pipenv install
py -m pipenv install django
py -m pipenv install django-cors-headers
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
py manage.py startapp greeting
```

Look at the files again, and make sure that you made the directory `greeting`.


## Part 3: Our First JSON Response <a name="json-response"></a>

First, we need to create a `urls.py` file inside of our app folder. Make the file `greeting/urls.py`, which should look like this:

```python
from django.urls import path
from django.http import JsonResponse

def greet_function(request):
       greet_text = "Hi there! I like the musical artist ______!"
       return JsonResponse({
               'greeting': greet_text,
       })

urlpatterns = [
    path('music/', greet_function),
]
```

The `urlpatterns` at the bottom should parse the url path, and if the pattern `music/` matches, it will send the request to the `greet_function` function, and run that to generate a JsonResponse.

Then, let's make our app urls accessable from our project urls. Make sure that `project/urls.py` looks like this:

```python
from django.contrib import admin
from django.urls import path, include # Changed line

urlpatterns = [
    path('admin/', admin.site.urls),
    path('greet/', include('greeting.urls')), # New line
]
```

Now, we need a frontend, which we will run as a separate server. Let's make a new directory next to `manage.py`, and we will call it `frontend`. Our directory should look like this:


```
frontend
greeting
manage.py
Pipfile
Pipfile.lock
project
```

Inside of frontend we can make a file called `index.html`, which should look like this:

```html
<!DOCTYPE html>
<html>
        <head>
                <meta charset="utf-8">
                <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
        </head>
        <body>
                <div id="output"></div>
                <script>
                        let outputDiv = document.querySelector("#output");
                        axios({
                                        method: 'get',
                                        url: 'http://localhost:8000/greet/music/',
                        }).then(
                                function(response) {
                                                outputDiv.innerText = response.data.greeting
                                }
                        )
                </script>
        </body>
</html>
```

This HTML file will make a `get` request through `ajax`, and use the resulting JSON response to determine the text that should be in our div.

Now, we will need two terminals opened to do the next part. The worst part is that we will probably get an error, so it won't work immediately. One terminal (the one with pipenv activated) should run the django server with the command

```
py manage.py runserver
```

With the other terminal, you should `cd` into frontend, and then run the following command:

```
py -m http.server 8001
```

This will run a server on port 8001.

With that command, you should be able to make `index.html` available on port `8001`, which means this link should work: <http://localhost:8001/index.html>

Unfortunately, we haven't properly set up CORS, which gives the browser permission to access our django server. You can look in the js console to see this error. We should have installed `django-cors-headers` in the first part of the tutorial, but we haven't modified our `settings.py` to use `django-cors-headers`.

```python
DEBUG = True

ALLOWED_HOSTS = ['*'] # Changed line

# Application definition

INSTALLED_APPS = [
```

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

Now, if we test it out, we should see our greeting.

## Part 4: Getting a List of Animals<a name="list-animals"></a>

Now, let's try to get a list of animals instead of a greeting. First, we can create a new app called `animals`:

```
py manage.py startapp animals
```

And, whenever we do this, we need to modify our `project/urls.py`:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('greet/', include('greeting.urls')),
    path('animals/', include('animals.urls')),
]
```

We can create the file `animals/urls.py`, which will handle basically everything in our app:

```python
from django.urls import path
from django.http import JsonResponse

animals = '''
alligator
ant
bear
bee
bird
camel
cat
cheetah
chicken
chimpanzee
cow
crocodile
deer
dog
dolphin
duck
eagle
elephant
fish
fly
fox
frog
giraffe
goat
goldfish
hamster
hippopotamus
horse
kangaroo
kitten
lion
lobster
monkey
octopus
owl
panda
pig
puppy
rabbit
rat
scorpion
seal
shark
sheep
snail
snake
spider
squirrel
tiger
turtle
wolf
zebra
'''.split()

def animals_function(request):
    return JsonResponse({
        'animals': animals,
    })

urlpatterns = [
    path('', animals_function),
]
```

Some students really commit to never copying and pasting from my examples, and this big list of animals will really test their commitment to that rule.


We can also change our `index.html` to prepare it to receive this information:

```html
       </head>
       <body>
               <div id="output"></div>
               <ul id="animals"></ul> # New line
               <script>
                       let outputDiv = document.querySelector("#output");
                       let animals = document.querySelector("#animals"); # New line
                       axios({
                                       method: 'get',
                                       url: 'http://localhost:8000/animals/', # Changed line
                       }).then(
                               function(request) {
                                               outputDiv.innerText = request.data.greeting # Deleted line
                                       console.log(request.data); # New line
                                       let animalsArr = request.data.animals; # New line
                                       for (let i=0; i<animalsArr.length; i++) { # New line
                                               let animal = animalsArr[i]; # New line
                                               animalLi = document.createElement("li"); # New line
                                               animalLi.innerText = animal; # New line
                                               animals.appendChild(animalLi); # New line
                                       } # New line
                               }
                       )
               </script>
```

Now, if we go back to our site, we should see a bunch of animals in a list. <http://localhost:8001/index.html>

## Part 5: Adding Vuejs<a name="adding-vue"></a>

Now, instead of using our old html file, let's move on to a new html file that uses VueJS. From now on we won't use the old html file anymore. We can make a new file, `index_vue.html`:

```html
<!DOCTYPE html>
<html>
       <head>
               <meta charset="utf-8">
               <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
               <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
       </head>
       <body>
               <div id="app">
                       <ul id="animals">
                               <li v-for="animal in animals">
                                       {{ animal }}
                               </li>
                       </ul>
               </div>
               <script>
                       var app = new Vue({
                               el: "#app",
                               data: {
                                       animals: [],
                               },
                       });
                       axios({
                                       method: 'get',
                                       url: 'http://localhost:8000/animals/',
                       }).then(
                               function(request) {
                                       console.log(request.data);
                                       app._data.animals = request.data.animals;
                               }
                       )
               </script>
       </body>
</html>
```
First, let's test this out by going to this link: <http://localhost:8001/index_vue.html>


If that works, then let's look at this `index_vue.html` file. The first thing to note is that we added a script at the top, which gives us access to the `Vue` class. That allows us to do this:

```js
var app = new Vue({
        el: "#app",
        data: {
                animals: [],
        },
});
```

This creates an instance of the Vue class, which will automatically do a bunch of stuff. When we say `el: "#app",`, we tell Vue to look for the HTML element with the id `app`. We have a div with the id `app`, and that is the div that our Vue instance gets tangled up in. Inside that div we use some weird syntax, and Vue knows how to interpret that syntax because it is tangled up with that div.

```js
<div id="app">
        <ul id="animals">
                <li v-for="animal in animals">
                        {{ animal }}
                </li>
        </ul>
</div>
```

We have our div with the id "app", so our Vue instance will look inside this div. We use Vue's weird for-loop syntax to loop over animals. We can reference animals because it is in the `data` object when we start the instance above.

```js
axios({
                method: 'get',
                url: 'http://localhost:8000/animals/',
}).then(
        function(request) {
                console.log(request.data);
                app._data.animals = request.data.animals;
        }
)
```

We get the list of animals from our server. The important thing is that setting `app._data.animals` will change the data in our app, and Vue will automatically update our for loop.

Here are some things we can do to get weird results:
* We can open up the javascript console in our browser, and we can write `app._data.animals = [1, 2, 3]`
  * This will change the data, and Vue will automatically update our for loop
* We can change `<div id="app">` to `<div id="something-else">`
  * This will result in Vue not interpreting that div as the div it should get tangled up in, so all the weird Vue syntax won't be used by Vue and will be left behind.
* We can put `{{ animals }}` inside the div and outside the div
  * The double curly is the delimiter, so that is how Vue knows that it should be looking at this as something to change. If we put it inside the div, then vue will replace it with the list of animals it has in its data. If we put it outside the div, Vue will not see it, and so we will just see the text `{{ animals }}`
* We can remove the double curlies around `{{ animal }}`
  * We should have a list with a bunch of items that say literally `animal`. We should have the same number of list items as there are animals in the animal list. We can't see the actual animal names because Vue sees this as something to change: `{{ animal }}`, but Vue does not see this as something to change: `animal`. Vue will only try to interpret something if it has delimiters around it.

## Part 6: Adding a Lifecycle Hook<a name="adding-hook"></a>

We can move stuff around a bit in our `index_vue.html` file like this:

```html

                               data: {
                                       animals: [],
                               },
                               created: function() { # New line
                                       axios({ # New line
                                                       method: 'get', # New line
                                                       url: 'http://localhost:8000/animals/', # New line
                                       }).then( # New line
                                               function(request) { # New line
                                                       console.log(request.data); # New line
                                                       app._data.animals = request.data.animals; # New line
                                               } # New line
                                       ) # New line
                               } # New line
                       });
                       axios({ # Deleted line
                                       method: 'get', # Deleted line
                                       url: 'http://localhost:8000/animals/', # Deleted line
                       }).then( # Deleted line
                               function(request) { # Deleted line
                                       console.log(request.data); # Deleted line
                                       app._data.animals = request.data.animals; # Deleted line
                       }); # Deleted line
               </script>
       </body>
</html>
```

`created` is a lifecycle hook. Basically, at various points of our app being created, mounted, updated, and deleted, we can tell it to do stuff. Right now we are telling it to send that request right after it's created, and update its data once it gets a response.

Now we're ready to do the final step, the search function.


## Part 7: Adding a Search Function<a name="search-function"></a>

First, we need to add some stuff to our `animals/urls.py`:

```python
def animals_function(request):
       return JsonResponse({
               'animals': animals,
       })

def filter_function(request): # New line
       print(request.get_raw_uri()) # New line
       data = request.GET # New line
       animals_filtered = [animal for animal in animals if animal.startswith(data['filterText'])] # New line
       print(animals_filtered) # New line
       return JsonResponse({ # New line
               'animals': animals_filtered, # New line
       }) # New line

urlpatterns = [
    path('', animals_function),
    path('filter/', filter_function), # New line
]
```

Now we have a function that can return a smaller list. It will pull the variable `filterText` from our query parameters. This will make more sense in a moment, when we actually use it.

If you ever want to have a function that's similar to this, but it filters out information from the database, you'll probably want to do that in your `views.py` (we are just using `urls.py` because we have a small app and don't want to think too much). You can use Django's queryset API, which you can read about [here](https://docs.djangoproject.com/en/3.0/ref/models/querysets/). You would probably want something similar to this example from that documentation:

```python3
>>> Blog.objects.filter(name__startswith='Beatles')
<QuerySet [<Blog: Beatles Blog>]>
```

Now we just need to change our frontend to use our new url path.

First, we can create a new html input element that will interact with Vue:
```html
               <div id="app">
                       <input id="filter" v-on:keydown="filterAnimals"> # New line
                       <ul id="animals">
                               <li v-for="animal in animals">
```

This is telling Vue that whenever someone pushes a key down on our input, the method filterAnimals should run. That method does not exist, so let's create it.
```html
                               data: {
                                       animals: [],
                               },
                               methods: { # New line
                                       filterAnimals: function(event) { # New line
                                               console.log(event); # New line
                                               let filterTextVar = event.target.value + event.key; # New line
                                               axios({ # New line
                                                               method: 'get', # New line
                                                               url: 'http://localhost:8000/animals/filter/', # New line
                                                               params: { # New line
                                                                       filterText: filterTextVar, # New line
                                                               } # New line
                                               }).then( # New line
                                                       function(request) { # New line
                                                               console.log(request.data); # New line
                                                               app._data.animals = request.data.animals; # New line
                                                       } # New line
                                               ) # New line
                                       }, # New line
                               }, # New line
                               created: function() {
                                       axios({
                                                       method: 'get',
```


Let's look at this new method that runs whenever you push a key down. It will take in the event, which is a big object full of relavent information. The important info for us is, what was in the box before you pushed a new letter, and what letter did you push? Add those together, and they make up the beginning of all acceptable words in our filter. Next, we use axios to send a get request, with `filterText: filterTextVar` in our parameters.

If you type `ch` into the box, then it will construct a full `uri` (uniform resource identifier) that looks like this: `http://localhost:8000/animals/filter/?filterText=ch`. The `ch` will be a combination of the `c` that it pulls out of `event.target.value`, and the `h` that was just pushed down and grabbed from `event.key`, that the variable `filterTextVar` gets assigned to.

In the `then` function, which runs when we get something back from our server, we change `animals` in our data, and Vue will automatically update the for loop.

Now, let's go back to `urls` and look at that function again.

```python
def filter_function(request):
       print(request.get_raw_uri())
       data = request.GET
       animals_filtered = [animal for animal in animals if animal.startswith(data['filterText'])]
       print(animals_filtered)
       return JsonResponse({
               'animals': animals_filtered,
       })
```

We have a line here, that says `print(request.get_raw_uri())`, and that should print out the full `uri` if we look in the terminal where we ran `py manage.py runserver`. It should look something like this: `http://localhost:8000/animals/filter/?filterText=ch`. Django is nice enough to put everything to the right of the question mark into a dictionary, so we end up with a dictionary that is similar to this:

```python
{
	'filterText': 'ch'
}
``` 
So we can get what the user typed by getting whatever the value is associated with the key `'filterText'`. That is what we are using to filter our list here: `if animal.startswith(data['filterText'])`.

There's still a lot to do: backspace doesn't work properly, and a lot of keys will cause weird errors. But this is a good start!
