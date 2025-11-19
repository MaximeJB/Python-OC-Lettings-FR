"""Tests for Profile model.

This module contains tests for the Profile model in the profiles application.
"""
from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import Profile


class ProfileModelTest(TestCase):
    """Test cases for the Profile model."""

    def test_create_profile(self):
        """Test that a profile can be created and saved correctly.

        Creates a user and profile, then verifies the profile is saved
        with the correct attributes.

        Asserts:
            Profile count equals 1.
            Profile favorite_city equals 'Paris'.
        """
        user = User.objects.create(username='testuser')
        profile = Profile.objects.create(user=user, favorite_city='Paris')
        self.assertEqual(Profile.objects.count(), 1)
        self.assertEqual(profile.favorite_city, 'Paris')

    def test_profile_str(self):
        """Test that profile string representation returns username.

        Creates a profile and verifies its __str__ method returns
        the associated user's username.

        Asserts:
            String representation equals 'johndoe'.
        """
        user = User.objects.create(username='johndoe')
        profile = Profile.objects.create(user=user, favorite_city='New York')
        self.assertEqual(str(profile), 'johndoe')
