"""Admin configuration for the profiles application.

This module registers Profile model in the Django admin interface.
"""
from django.contrib import admin

from .models import Profile

admin.site.register(Profile)
