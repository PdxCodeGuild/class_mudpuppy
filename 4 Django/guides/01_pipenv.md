[//]: # (
    TODO:
)

# Using Pipenv

## Introduction

This tutorial will help us use `pipenv`, which lets us organize the python files that we depend on.

## Part 1
### Using Pip

`Pip` is an acronym for "pip installs packages". `Pip` can help us install python files that we can depend on. A good example of a package we've used is the `random.py` file. You have used this file whenever you've run any python like this:

```python
import random
print(random.choice('abc'))
```

`random.py` automatically comes whenever you download python.

If we want to use a package that doesn't automatically come with python, we can use `pip`. First, let's see what commands `pip` understands:

```
py -m pip help
```

`py` is our python interpreter, `-m` means use a module (a module is like a piece of a package), and then `pip` installs packages. `Pip` understands many additional commands.

We should try installing the package `cowsay`. First, we can search for the package `cowsay` with this command:

```
py -m pip search cowsay
```

It should show a package we can install:
```
cowsay (2.0.3)               - The famous cowsay for GNU/Linux is now
                               available for python
```

Now we can install it with the command:
```
py -m pip install cowsay
```

And we can use the cowsay module:
```
py -m cowsay "mooo"
```

`Pip` put the cowsay module somewhere, and we can see where it is by running:

```
py -c "import cowsay; print(cowsay.__file__)"
```

My cowsay file is here:

```
/home/atb-codeguild/.local/lib/python3.8/site-packages/cowsay/__init__.py
```

That last `cowsay` folder is a package, and all the files inside that folder are modules.

## Part 2
### Messing with Pipenv

Now let's install pipenv and mess with it!

Run this command:

```
py -m pip install pipenv
```

Now make a new directory in your file explorer and `cd` into it. Once you've done that, you can run the following commands:

```py -m pipenv install```

and

```py -m pipenv install cowsay```

and

```py -m pipenv shell```

These commands probably looked pretty weird. We should still be able to use cowsay with the following command:
```
py -m cowsay "oink"
```

We can see the cowsay package by running this:

```
py -c "import cowsay; print(cowsay.__file__)"
```
Now you should see a different location than the previous one. This folder now has its own cowsay file in its own obscure location.

You should also have a Pipfile that looks like this:


```pipfile
[[source]]
name = "pypi"
url = "https://pypi.org/simple"
verify_ssl = true

[dev-packages]

[packages]
cowsay = "*"

[requires]
python_version = "3.8"
```

Yours might have a different python version, I assume you're using a less cool version than I'm using.

The Pipfile.lock is useful if you want to have strict version control on all your packages, so that you don't have to worry about someone updating cowsay and breaking your entire cowsay-based project.

If you share a python project with others, it's good to also share a Pipfile, so that they can easily create a specific environment that is similar to your environment. If your Pipfile referred to a long list of packages, someone using pipenv could easily install all those packages in one command, and those packages would be put in an out-of-the-way location so that they won't overwrite the main package files.

Generally, whenever you start a project that depends on python packages, such as a Django project, you should create a pipenv virtual environment for that folder.