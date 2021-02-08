from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import Movie, Service, Profile, User
from . import urls
from .forms import ProfileForm, EditProfileForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def films(request):
    movies = Movie.objects.all()
    context = { 'movies': movies}
    return render(request, 'films.html', context)

@login_required
def services(request):
    services = Service.objects.all()
    context = { 'services': services }
    print(services)
    return render(request, 'services.html', context)

def search_movie(request):
    movies = ''
    query = request.POST['query']
    movies = Movie.objects.filter(Q(title__icontains=query))
    if len(movies) == 1:
        return redirect('film_detail', movie_id=movies[0].id)
    else:
        return render(request, 'search_results.html', {'movies': movies})

def film_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    is_subscribed = False   
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        for film in profile.fav_movies.all():
            if film == movie:
                print('movie is saved in favs')
                if request.method == 'POST':
                    profile.fav_movies.remove(movie)
                    profile.save()
                    # .pop(movie).save()
                    print('movie removed from favs')
                    return redirect('profile')
        if request.method == 'POST':
            profile.fav_movies.add(movie)
            return redirect('profile')
        for film in profile.fav_movies.all():
            if film == movie:
                is_subscribed = True
    else:
        profile: ''
    context = {
        'is_subscribed': is_subscribed,
        'movie': movie,
        'profile': profile
    }
    
    return render(request, 'film_detail.html', context)

@login_required
def add_services(request):
    profile = Profile.objects.get(user=request.user)
    services = Service.objects.all()
    context = {
        'profile': profile,
        'services': services
    }
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        profile.subbed_services.add(request.POST['service'])
        return render(request, 'add_services.html', context)
    return render(request, 'add_services.html', context)

@login_required
def remove_services(request, profile):
    pass
#     if request.method == 'POST':
#         profile.subbed_services.remove(request.POST).save()
#     return redirect('edit_profile')

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

@login_required
def profile(request):
    if not Profile.objects.filter(user=request.user):
        return redirect('create_profile')
    else:
        profile = Profile.objects.get(user=request.user)
        print('********************', profile.subbed_services.all)
        context = {
            'profile': profile
        }
        return render(request, 'profile.html', context)

@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
        context = {'form': form}
        return render(request, 'edit_profile.html', context)
    
    else:
        filled_form = EditProfileForm(request.POST, instance=profile)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('profile')
        

            