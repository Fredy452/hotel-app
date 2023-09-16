"""User URLs."""

# Django
from django.urls import path

# Views
from apps.user.views import user_login, register

app_name = "user"

urlpatterns = [
    path("login/", user_login, name="login"),
    path("register/", register, name="register"),
]