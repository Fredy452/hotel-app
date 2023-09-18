"""User URLs."""

# Django
from django.urls import path

# Views
from apps.user.views import user_login, register, user_profile, user_logout, user_profile_updated

app_name = "user"

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("profile/<int:user_id>/<str:username>/show", user_profile, name="profile"),
    path('profile/<int:user_id>/<str:username>/updated', user_profile_updated, name="updated")
]