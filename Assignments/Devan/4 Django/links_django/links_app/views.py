from django.shortcuts import render
from .models import Link


# Create your views here.


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
