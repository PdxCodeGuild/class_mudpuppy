from django.shortcuts import render, reverse # Changed line
from django.http import HttpResponseRedirect # New line
from .models import Link, Comment

def index(request):
    all_links = Link.objects.all()
    context = {
        'all_links_template': all_links,
    }
    return render(request, 'links_app/index.html', context)

def link_slug(request, in_slug):
    found_link = Link.objects.get(slug=in_slug)
    comments = found_link.comment_set.all()
    context = {
        'found_link': found_link,
    }
    return render(request, 'links_app/slug.html', context)

def add_comment(request):
    data = request.POST
    new_comment = Comment(
        ink_id = data['link'],
        text = data['commenttext'],
    )
    new_comment.save()
    link_slug = Link.objects.get(id=data['link']).slug
    return HttpResponseRedirect(reverse('links_paths:slug_path', args=[link_slug]))