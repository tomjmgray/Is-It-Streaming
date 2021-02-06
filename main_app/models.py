from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    def __str__(self):
        return self.title
    
class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100,default='Free')
    library = models.ManyToManyField(Movie)
    def __str__(self):
        return self.name
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fav_movies = models.ManyToManyField(Movie, blank=True, null=True)
    subbed_services = models.ManyToManyField(Service, blank=True, null=True)