from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, Service
from . import urls

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

def search_movie(request):
    query = request.POST['query']
    movies = Movie.objects.filter(title__contains=query)
    if movies:
        return render(request, 'search_results.html', {'movies': movies})

    
    # query = request.POST.query
    # results = Movie.objects.filter(name__icontains=query)
    # context = {'results': results}
    # return render(request, 'search_results', context)

        