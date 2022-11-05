# Custom User Model process referenced from:
# https://testdriven.io/blog/django-custom-user-model/

from django.urls import path
from . import views
from .views import SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    # Xbox Anticipator code - urls:
    path('', views.GameList.as_view(), name='index'),
    path('<slug:slug>/', views.GameDetail.as_view(), name='game_detail'),
]
