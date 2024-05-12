from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context: dict[str, str] = {
        'title': 'Home',
        'content': 'Main store page - HOME',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'is_authenticated': False
    }
    return render(request, 'main/index.html')

def about(request):
    return HttpResponse('About page')