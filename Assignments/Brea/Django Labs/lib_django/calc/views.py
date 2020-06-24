from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
base = '''
<body style="height:100vh;width100vs;background-color:lemonchiffon">
<h1>{type} Results</h1>
<h3>{results}</h3>
</body>
'''

def add(request, num1, num2):
    return HttpResponse(
        base.format(
            type='Addition',
            results=num1+num2,
        )
    )

def sub(request, num1, num2):
    return HttpResponse(
        base.format(
            type='Subtraction',
            results=num1-num2
        )
    )