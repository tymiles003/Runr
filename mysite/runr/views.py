from django.http import Http404
from django.shortcuts import render, get_object_or_404

from runr.models import Timer
from runr.utils import id_generator

def index(request):
    return render(request, 'index.html')

def new_timer(request):
    id = id_generator()
    return render(request, 'detail.html', {'key':id})

def show_timer(request, key):
    timer = get_object_or_404(Timer, pk=key)
    return render(request, 'detail.html', {'key':key})
