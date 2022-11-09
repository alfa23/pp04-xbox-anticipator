# Custom User Model process referenced from:
# https://testdriven.io/blog/django-custom-user-model/

from django.urls import path
from . import views
from .views import SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    # Xbox Anticipator code - urls:
    path('', views.GameList.as_view(), name='index'),
    path('create/', views.GameCreateView.as_view(), name='game_create'),
    path('update/<slug:slug>/', views.GameUpdateView.as_view(), name='game_update'),
    # path('delete/', views.GameDeleteView.as_view(), name='game_delete'),
    path('<slug:slug>/', views.GameDetail.as_view(), name='game_detail'),
]
