# Custom User Model process referenced from:
# https://testdriven.io/blog/django-custom-user-model/

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.views import generic
from .models import Game


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


# Xbox Anticipator code - views:


class GameList(generic.ListView):
    model = Game
    queryset = Game.objects.filter(status=1).order_by('release_date')
    template_name = 'index.html'
    paginate_by = 6
