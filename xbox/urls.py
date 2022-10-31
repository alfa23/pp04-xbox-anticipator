# Custom User Model process referenced from:
# https://testdriven.io/blog/django-custom-user-model/

from django.urls import path

from .views import SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]
