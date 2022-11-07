# Custom User Model process referenced from:
# https://testdriven.io/blog/django-custom-user-model/

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import SignupForm
from django import forms
from .models import CustomUser, Game, Comment


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')


# Xbox Anticipator code - forms:

# Settings for CustomUser email as username in Django-AllAuth, sourced from:
# https://pyphilly.org/know-thy-user-custom-user-models-django-allauth/


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=150, label='First Name')
    last_name = forms.CharField(max_length=150, label='Last Name')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


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
            'feature_image',
            # 'status',
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
