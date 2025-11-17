"""Tests for profile views.

This module contains tests for the profiles application views.
"""
import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestProfileViews:
    """Test cases for profile-related views."""

    def test_profile_index(self, client):
        """Test that profiles index page returns 200 status code.

        Args:
            client: Django test client fixture.
        """
        response = client.get(reverse('profiles_index'))
        assert response.status_code == 200

    def test_profile_detail(self, client, profile):
        """Test that profile detail page returns 200 status code.

        Args:
            client: Django test client fixture.
            profile: Profile fixture from conftest.
        """
        response = client.get(reverse('profile', args=[profile.user.username]))
        assert response.status_code == 200
