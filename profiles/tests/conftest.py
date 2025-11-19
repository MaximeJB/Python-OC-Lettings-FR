"""Pytest fixtures for the profiles application tests.

This module provides shared test fixtures for profile-related tests.
"""
import pytest
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.fixture
def user():
    """Create a test user.

    Returns:
        A Django User instance for testing.
    """
    return User.objects.create(username='testuser', password='testpass')


@pytest.fixture
def profile(user):
    """Create a test profile associated with a user.

    Args:
        user: User fixture to associate with the profile.

    Returns:
        A Profile instance for testing.
    """
    return Profile.objects.create(user=user, favorite_city='Paris')
