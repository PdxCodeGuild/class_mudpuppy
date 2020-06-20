from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# lines 1 -5 are your actual web pages that you display through your server.

