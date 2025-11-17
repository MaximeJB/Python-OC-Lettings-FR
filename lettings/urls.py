"""URL configuration for the lettings application.

This module defines URL patterns for letting-related views.
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.lettings_index, name='lettings_index'),
    path('<int:letting_id>/', views.letting, name='letting'),
]
