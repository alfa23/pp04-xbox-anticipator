# Custom User Model process referenced from:
# https://testdriven.io/blog/django-custom-user-model/

from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm, GameForm
from django.views import generic, View
from .models import Game, Rating, Comment, CustomUser


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


class GameDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Game.objects.filter(status=1)
        game = get_object_or_404(queryset, slug=slug)
        commenters = game.commenters_tally.count()
        comments = game.comments.filter(approved=True).order_by('posted_on')
        liked = False
        # if game.likes.filter(id=self.request.user.id).exists():
        #     liked = True

        return render(
            request,
            'game_detail.html',
            {
                'game': game,
                'commenters': commenters,
                'comments': comments,
                'liked': liked
            }
        )


class GameCreateView(CreateView):
    model = Game
    form_class = GameForm
    template_name = 'game_create.html'
    success_url = reverse_lazy('index')
