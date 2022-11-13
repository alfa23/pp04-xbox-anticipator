# Custom User Model process referenced from:
# https://testdriven.io/blog/django-custom-user-model/

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import SignupForm
from django import forms
from django.forms.widgets import DateInput, NumberInput
from .models import CustomUser, Game, Comment, Rating


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
    first_name = forms.CharField(
        max_length=150, label='First Name',
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        max_length=150, label='Last Name',
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})
    )

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user

# DateInput CBV created to enable date picker in Django, sourced from:
# https://stackoverflow.com/questions/3367091/whats-the-cleanest-simplest-to-get-running-datepicker-in-django


# class DateInput(forms.DateInput):
#     input_type = 'date'


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = [
            'title',
            # 'slug',
            'dev_pub',
            'release_date',
            'website',
            'game_info',
            'info_excerpt',
            'feature_image',
            # 'status',
        ]
        widgets = {
            'release_date': DateInput(attrs={'type': 'date'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', ]


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rate', ]
        widgets = {
            'rate': NumberInput,
        }


# class RatingForm(forms.Form):
#     rate = forms.DecimalField(
#         required=True,
#         label=False,
#         widget=forms.TextInput(
#             attrs={
#                 'step': '0.1',
#                 'type': 'range',
#                 'value': '0.5',
#                 'min': '0',
#                 'max': '5',
#             }
#         )
#     )
