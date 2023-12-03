from django.urls import path
from authentication.views import *

app_name = 'authentication'

urlpatterns = [
    path("login/", login_user, name="login_user"),
    path("register/", register, name="register"),
    path("logout/", logout_user, name="logout_user")
]