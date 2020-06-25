from django.shortcuts import render
from django.http import HttpResponse

base = '''
<body style="height:100vh;width:10vw;background-color:lemonchiffon">
<h1>{type} Results</h1>
<h3>{results}</h3>
</body>
'''

def add(rquest, num1, num2):
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
            results=num1-num2,
        )
    )

# Create your views here.
