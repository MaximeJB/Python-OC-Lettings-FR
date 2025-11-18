"""Views for the profiles application.

This module contains views to display user profiles list and individual profile details.
"""
import logging
from django.shortcuts import render
from django.http import Http404
from .models import Profile

logger = logging.getLogger(__name__)


def index(request):
    """Display list of all user profiles.

    Args:
        request: HTTP request object.

    Returns:
        HttpResponse: Rendered template with list of profiles.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    logger.info("Profiles index page accessed")
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """Display details of a specific user profile.

    Args:
        request: HTTP request object.
        username: Username of the profile to display.

    Returns:
        HttpResponse: Rendered template with profile details.

    Raises:
        Http404: If profile with given username does not exist.
    """
    try:
        profile = Profile.objects.get(user__username=username)
        logger.info(f"Profile {username} accessed successfully")
    except Profile.DoesNotExist:
        logger.error(f"Profile with username {username} not found")
        raise Http404("Profile not found")
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
