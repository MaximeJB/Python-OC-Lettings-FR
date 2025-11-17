"""Application configuration for the profiles application.

This module contains the Django AppConfig for the profiles app.
"""
from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """Configuration class for the profiles application.

    Attributes:
        default_auto_field: Default primary key field type.
        name: Name of the application.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "profiles"
