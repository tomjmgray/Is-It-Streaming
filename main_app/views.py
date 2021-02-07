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
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        profile.fav_movies.add(movie)
        return redirect('profile')
    # streaming = []
    # for service in movie.service_set.objects.all():
    #     streaming.append(service)
    print('**********************')
    print(movie.service_set.all)
    context = {
        'movie': movie,
    }
    return render(request, 'film_detail.html', context)

def add_services(request):
    services = Service.objects.all()
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        profile.subbed_services.add(request.POST['service'])
        return render(request, 'add_services.html', {'services': services})
    return render(request, 'add_services.html', {'services': services})

def signup(request):
    error_message: ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print('User created!')
            login(request, user)
            
        else:
            error_message = 'Invalid credentials, please enter valid credentials and try again.'
            print('Error creating user')
    form = UserCreationForm()
    context = {
        'form': form,
        # 'error_message': error_message
    }
    return render(request, 'registration/register.html', context)

def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            print('Form is valid')
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            print(profile.user)
            # profile.user = request.user.id
            return redirect('profile')
    services = Service.objects.all()
    form = ProfileForm()
    context = {
        'form': form,
        'services': services
    }
    return render(request, 'create_profile.html', context)

def profile(request):
    if not request.user.is_authenticated:
        return redirect('create_profile')
    else:
        profile = Profile.objects.get(user=request.user)
        print('********************', profile.subbed_services.all)
        context = {
            'profile': profile
        }
        return render(request, 'profile.html', context)

def edit_profile(request):
    if request.method == 'POST':
        return render(request, 'edit_profile.html')
    
        

            