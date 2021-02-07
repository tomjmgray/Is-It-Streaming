from django import forms
from .models import Movie, Service, Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields = [
            'first_name',
            'last_name'
        ]
