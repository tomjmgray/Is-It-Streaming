from django import forms
from .models import Movie, Service, Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'fav_movies',
            'subbed_services'
        ]
