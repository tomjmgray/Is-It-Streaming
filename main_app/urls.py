from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('films/', views.films, name="films"),
    path('films/<int:movie_id>/', views.film_detail, name='film_detail'),
    path('services/', views.services, name="services"),
    path('add_services/', views.add_services, name="add_services"),
    path('remove_services/', views.remove_services, name="remove_services"),
    path('search_movie/', views.search_movie, name="search_movie"),
    path('accounts/signup/', views.signup, name='signup'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('delete_profile', views.delete_profile, name='delete_profile'),
    path('profile/', views.profile, name='profile')
]