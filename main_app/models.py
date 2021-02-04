from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    def __str__(self):
        return self.title
    

# godfather = Movie('The Godfather', 1972, 'Sling')
# goodfellas = Movie('Goodfellas', 1990, 'Netflix')
# casino = Movie('Casino', 1995, ['Peacock', 'Sling'])
# the_irishman = Movie('The Irishman', 2019, 'Netflix')

# movies = [
#     godfather,
#     goodfellas,
#     casino,
#     the_irishman
# ]

class Service(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
