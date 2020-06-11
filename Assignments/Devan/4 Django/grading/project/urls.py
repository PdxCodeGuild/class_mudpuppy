from django.contrib import admin
from django.urls import path
from django.http import JsonResponse


def movie_fun(request):
    return JsonResponse({'message': 'I like the movie The Big Lebowski'})


def grading_fun(request):
    print(request.GET)
    grade_num = request.GET['grade']
    grade_num = int(grade_num)
    grade_let = ''
    if grade_num > 90:
        grade_let = 'A'
    elif grade_num > 80:
        grade_let = 'B'
    elif grade_num > 70:
        grade_let = 'C'
    elif grade_num > 60:
        grade_let = 'D'
    else:
        grade_let = 'F'
    return JsonResponse({'grade': grade_let})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', movie_fun),
    path('grading/', grading_fun),



]
