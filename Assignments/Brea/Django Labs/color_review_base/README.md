# Color Reviews

## Concepts

Number reviews, average review score, highest review score

## Instructions

Run:

```
py -m pipenv install
py -m pipenv shell
py manage.py makemigrations
py manage.py migrate
py manage.py populate_colors
py manage.py runserver
```

Reset recorded average review scores with:

```
py manage.py reset_avg
```
