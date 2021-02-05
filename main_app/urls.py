from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('films/', views.films, name="films"),
    path('services/', views.services, name="services"),
    path('search_movie/', views.search_movie, name="search_movie")
]