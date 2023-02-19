from django.urls import path
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh

from .views import (
    register,
    change_password,
    update_profile,
    logout,
    delete_profile,
)


namespace = "accounts"

urlpatterns = [
    path("login/", token_obtain_pair, name="token_obtain_pair"),
    path("login/refresh", token_refresh, name="token_refresh"),
    path("register/", register, name="register"),
    path("logout/", logout, name="logout"),
    path("delete-profile/", delete_profile, name="delete_profile"),
]
