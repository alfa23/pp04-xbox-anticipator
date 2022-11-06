# Custom User Model process referenced from:
# https://testdriven.io/blog/django-custom-user-model/

from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm, GameForm, CommentForm
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
        rating_total = 0
        rating_count = 0
        ratings = Rating.objects.filter(
            game=game
        ).all()
        print("Debugging here...")
        for _rating in ratings:
            rating_total += _rating.rate
            rating_count += 1
        if rating_count> 0:
            rating = rating_total / rating_count
        else:
            rating = 0
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
                'commented': False,
                'comment_form': CommentForm(),
                'liked': liked,
                'rating': rating
            }
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Game.objects.filter(status=1)
        game = get_object_or_404(queryset, slug=slug)
        commenters = game.commenters_tally.count()
        comments = game.comments.filter(approved=True).order_by('posted_on')
        liked = False
        # if game.likes.filter(id=self.request.user.id).exists():
        #     liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            # user_id = request.user.id
            comment_form.instance.email = request.user.email
            # comment_form.instance.name = user_id
            comment = comment_form.save(commit=False)
            comment.game = game
            comment.user = request.user
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            'game_detail.html',
            {
                'game': game,
                'commenters': commenters,
                'comments': comments,
                'commented': True,
                'comment_form': CommentForm(),
                'liked': liked
            }
        )


class GameCreateView(CreateView):
    model = Game
    form_class = GameForm
    template_name = 'game_create.html'
    success_url = reverse_lazy('index')
