# Custom User Model process referenced from:
# https://testdriven.io/blog/django-custom-user-model/

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser, Game


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')


# Xbox Anticipator code - forms:


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = [
            'title',
            'dev_pub',
            'release_date',
            'website',
            'game_info',
            'info_excerpt',
            'status',
        ]
