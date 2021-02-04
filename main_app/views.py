from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, Service

# Create your views here.
def home(request):
    return render(request, 'home.html')

def films(request):
    movies = Movie.objects.all()
    context = { 'movies': movies}
    return render(request, 'films.html', context)

def services(request):
    services = Service.objects.all()
    context = { 'services': services }
    print(services)
    return render(request, 'services.html', context)
        