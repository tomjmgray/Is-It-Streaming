from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie, Service, Profile, User
from . import urls
from .forms import ProfileForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

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
    if len(movies) == 1:
        return redirect('film_detail', movie_id=movies[0].id)
    elif movies:
        return render(request, 'search_results.html', {'movies': movies})

def film_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    # streaming = []
    # for service in movie.service_set.objects.all():
    #     streaming.append(service)
    print('**********************')
    print(movie.service_set.all)
    context = {
        'movie': movie,
        # 'services': streaming
    }
    return render(request, 'film_detail.html', context)

    
    # query = request.POST.query
    # results = Movie.objects.filter(name__icontains=query)
    # context = {'results': results}
    # return render(request, 'search_results', context)

def signup(request):
    error_message: ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')
        else:
            error_message = 'Invalid credentials, please enter valid credentials and try again.'
    form = UserCreationForm()
    context = {
        'form': form,
        # 'error_message': error_message
    }
    return render(request, 'registration/register.html', context)

def profile(request):
    return render(request, 'profile.html')


            