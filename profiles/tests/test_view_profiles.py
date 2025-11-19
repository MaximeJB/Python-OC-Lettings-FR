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

        Makes a GET request to the profiles index page and verifies
        the response status.

        Args:
            client: Django test client fixture.

        Asserts:
            Response status code equals 200.
        """
        response = client.get(reverse('profiles:index'))
        assert response.status_code == 200

    def test_profile_detail(self, client, profile):
        """Test that profile detail page returns 200 status code.

        Creates a profile using the fixture, makes a GET request to
        the profile detail page, and verifies the response status.

        Args:
            client: Django test client fixture.
            profile: Profile fixture from conftest.

        Asserts:
            Response status code equals 200.
        """
        response = client.get(reverse('profiles:profile', args=[profile.user.username]))
        assert response.status_code == 200

    def test_profile_detail_not_found(self, client):
        """Test that profile detail page returns 404 for non-existent user.

        Makes a GET request to a profile detail page with a username
        that doesn't exist and verifies a 404 response is returned.

        Args:
            client: Django test client fixture.

        Asserts:
            Response status code equals 404.
        """
        response = client.get(reverse('profiles:profile', args=['nonexistentuser']))
        assert response.status_code == 404
