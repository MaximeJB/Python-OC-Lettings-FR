"""Models for the lettings application.

This module defines the Address and Letting models used to store
property rental information.
"""
from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """Model representing a physical address.

    Attributes:
        number: Street number (max 9999).
        street: Street name.
        city: City name.
        state: State code (2 characters).
        zip_code: ZIP code (max 99999).
        country_iso_code: Country ISO code (3 characters).
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        """Return string representation of the address.

        Returns:
            str: Street number and name combined.
        """
        return f'{self.number} {self.street}'

    class Meta:
        verbose_name_plural = "Adresses"


class Letting(models.Model):
    """Model representing a property letting.

    Attributes:
        title: Title of the letting.
        address: One-to-one relationship with Address model.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """Return string representation of the letting.

        Returns:
            str: Title of the letting.
        """
        return self.title

    class Meta:
        verbose_name_plural = "Lettings"
