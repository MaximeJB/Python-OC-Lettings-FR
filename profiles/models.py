"""Models for the profiles application.

This module defines the Profile model used to store user profile information.
"""
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Model representing a user profile.

    Attributes:
        user: One-to-one relationship with Django User model.
        favorite_city: User's favorite city (optional).
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profiles_profile')
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """Return string representation of the profile.

        Returns:
            str: Username of the associated user.
        """
        return self.user.username

    class Meta:
        verbose_name_plural = "Profiles"
