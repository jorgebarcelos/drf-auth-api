from django.urls import path, re_path
from .views import *
from . import api


"""API Routes"""
urlpatterns = [
    re_path('login', api.login),
    re_path('signup', api.signup),
    re_path('test_token', api.test_token),
]


urlpatterns = [
    path('signup_view/', signup),
]