"""Tests for Profile model.

This module contains tests for the Profile model in the profiles application.
"""
from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import Profile


class ProfileModelTest(TestCase):
    """Test cases for the Profile model."""

    def test_create_profile(self):
        """Test that a profile can be created and saved correctly."""
        user = User.objects.create(username='testuser')
        profile = Profile.objects.create(user=user, favorite_city='Paris')
        self.assertEqual(Profile.objects.count(), 1)
        self.assertEqual(profile.favorite_city, 'Paris')

    def test_profile_str(self):
        """Test that profile string representation returns username."""
        user = User.objects.create(username='johndoe')
        profile = Profile.objects.create(user=user, favorite_city='New York')
        self.assertEqual(str(profile), 'johndoe')
