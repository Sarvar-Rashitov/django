"""Marshrut"""
from django.urls import path
from .views import *


urlpatterns = [
    path('<int:id>', homeView, name = 'home'),
]