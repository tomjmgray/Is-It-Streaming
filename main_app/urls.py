from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('films/', views.films, name="films"),
    path('films/<int:movie_id>/', views.film_detail, name='film_detail'),
    path('services/', views.services, name="services"),
    path('search_movie/', views.search_movie, name="search_movie"),
    path('accounts/signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile')
]