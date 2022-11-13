# Custom User Model process referenced from:
# https://testdriven.io/blog/django-custom-user-model/

from django.shortcuts import render, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.contrib import messages
# from django.contrib.messages.views import SuccessMessageMixin
from django.template.defaultfilters import slugify
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic, View
from .forms import CustomUserCreationForm, GameForm, CommentForm, RatingForm
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

        """ User rating """
        if request.user.is_authenticated:
            ratings = Rating.objects.filter(game=game).all()
            if ratings.filter(user=self.request.user).exists():
                # https://stackoverflow.com/questions/54815303/how-to-extract-data-from-django-queryset:
                current_user_queryset = ratings.filter(user=self.request.user)
                current_user_rating = current_user_queryset[0]
            else:
                current_user_rating = 0
        else:
            current_user_rating = 0

        """ Calculate average game rating and round to 1dp """
        rating_total = 0
        rating_count = 0
        ratings = Rating.objects.filter(game=game).all()
        for _rating in ratings:
            rating_total += _rating.rate
            rating_count += 1
        if rating_count > 0:
            rating_raw = rating_total / rating_count    # Calculate raw average
            rating_rounded = round(rating_raw, 1)       # and round to 1dp
        else:
            rating_rounded = 0

        return render(
            request,
            'game_detail.html',
            {
                'game': game,
                'commenters': commenters,
                'comments': comments,
                'commented': False,
                'comment_form': CommentForm(),
                'rating_form': RatingForm(),
                'rating_rounded': rating_rounded,
                'current_user_rating': current_user_rating,
            }
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Game.objects.filter(status=1)
        game = get_object_or_404(queryset, slug=slug)
        commenters = game.commenters_tally.count()
        comments = game.comments.filter(approved=True).order_by('posted_on')

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment = comment_form.save(commit=False)
            comment.game = game
            comment.user = request.user
            comment.save()
            messages.success(request, 'Comment posted successfully!')
        else:
            comment_form = CommentForm()

        """ Set or update user rating """
        current_user_rating = 0
        if request.POST.get('rate'):
            existing_user_rating = Rating.objects.filter(
                game=game,
                user=request.user,
            ).first()
            if existing_user_rating:
                existing_user_rating.rate = request.POST.get('rate')
                current_user_rating = existing_user_rating.rate
                existing_user_rating.save()
            else:
                current_user_rating = Rating(
                    game=game,
                    user=request.user,
                    rate=request.POST.get('rate')
                ).save()
            messages.success(request, 'Rating posted successfully!')

        """ User rating """
        ratings = Rating.objects.filter(game=game).all()
        if ratings.filter(user=self.request.user).exists():
            # https://stackoverflow.com/questions/54815303/how-to-extract-data-from-django-queryset:
            current_user_queryset = ratings.filter(user=self.request.user)
            current_user_rating = current_user_queryset[0]
        else:
            current_user_rating = 0

        """ Calculate average game rating """
        rating_total = 0
        rating_count = 0
        ratings = Rating.objects.filter(game=game).all()
        for _rating in ratings:
            rating_total += _rating.rate
            rating_count += 1
        if rating_count > 0:
            rating_raw = rating_total / rating_count    # Calculate raw average
            rating_rounded = round(rating_raw, 1)       # and round to 1dp
        else:
            rating_rounded = 0

        return render(
            request,
            'game_detail.html',
            {
                'game': game,
                'commenters': commenters,
                'comments': comments,
                'commented': True,
                'comment_form': CommentForm(),
                'rating_form': RatingForm(),
                'rating_rounded': rating_rounded,
                'current_user_rating': current_user_rating,
            }
        )


class GameCreateView(CreateView):
    model = Game
    form_class = GameForm
    template_name = 'game_create.html'

    def get_success_url(self):
        messages.success(self.request, 'Game data created successfully')
        current_slug = slugify(self.object)
        return reverse('game_detail', kwargs={'slug': current_slug})

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        f = form.save(commit=False)
        f.user = self.request.user
        f.creator = self.request.user
        f.save()
        return super(GameCreateView, self).form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(form=form))


class GameUpdateView(UpdateView):
    model = Game
    fields = [
        'dev_pub',
        'release_date',
        'website',
        'game_info',
        'info_excerpt',
        'feature_image'
    ]
    template_name = 'game_update.html'

    def get_success_url(self):
        messages.success(self.request, 'Game data updated successfully')
        current_slug = slugify(self.object)
        return reverse('game_detail', kwargs={'slug': current_slug})


class GameDeleteView(DeleteView):
    model = Game
    success_url = reverse_lazy('index')
    success_message = 'Game data deleted successfully'

    # Add success message method: https://stackoverflow.com/questions/24822509/
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(GameDeleteView, self).delete(request, *args, **kwargs)
