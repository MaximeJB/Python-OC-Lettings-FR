"""Application configuration for the lettings application.

This module contains the Django AppConfig for the lettings app.
"""
from django.apps import AppConfig


class LettingsConfig(AppConfig):
    """Configuration class for the lettings application.

    Attributes:
        default_auto_field: Default primary key field type.
        name: Name of the application.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "lettings"
