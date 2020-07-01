from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
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
        'found_link_template': found_link, 
        'comments_template': comments,
    }
    return render(request, 'links_app/slug.html', context)

def add_comment(request):
    data = request.POST
    new_comment = Comment(
        link_id = data['link'],
        text = data['commenttext'],
    )
    new_comment.save()
    link_slug = Link.objects.get(id=data['link']).slug
    return HttpResponseRedirect(reverse('links_paths:slug_path', args=[link_slug]))

# Create your views here.
