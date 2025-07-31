from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse("Hello, world. You're at the main index.")
    return render(request, 'main/index.html', {})

# Create your views here.
