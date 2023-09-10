from django.urls import re_path
from . import api


"""API Routes"""
urlpatterns = [
    re_path('login', api.login),
    re_path('signup', api.signup),
    re_path('test_token', api.test_token),
]
