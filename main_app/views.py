from django.shortcuts import render
from django.http import HttpResponse
from .models import movies

# Create your views here.
def home(request):
    return render(request, 'home.html')

def films(request):
    return render(request, 'films.html', { 'movies': movies })