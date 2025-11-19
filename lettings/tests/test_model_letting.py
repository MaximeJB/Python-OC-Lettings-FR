"""Tests for Address and Letting models.

This module contains tests for the Address and Letting models
in the lettings application.
"""
from django.test import TestCase
from lettings.models import Letting, Address


class AddressModelTest(TestCase):
    """Test cases for the Address model."""

    def test_create_address(self):
        """Test that an address can be created and saved correctly.

        Creates an address with all required fields and verifies
        it is saved to the database with correct attributes.

        Asserts:
            Address count equals 1.
            Address city equals 'Paris'.
        """
        address = Address.objects.create(
            number=2,
            street='Rue de Paris',
            city='Paris',
            state='Fr',
            zip_code=75000,
            country_iso_code='FRA'
        )
        self.assertEqual(Address.objects.count(), 1)
        self.assertEqual(address.city, 'Paris')

    def test_address_str(self):
        """Test that address string representation returns number and street.

        Creates an address and verifies its __str__ method returns
        the formatted address as 'number street'.

        Asserts:
            String representation equals '2 Rue de Paris'.
        """
        address = Address.objects.create(
            number=2,
            street='Rue de Paris',
            city='Paris',
            state='Fr',
            zip_code=75000,
            country_iso_code='FRA'
        )
        self.assertEqual(str(address), '2 Rue de Paris')


class LettingModelTest(TestCase):
    """Test cases for the Letting model."""

    def test_create_letting(self):
        """Test that a letting can be created with an address.

        Creates an address and a letting linked to it, then verifies
        the letting is saved with correct attributes.

        Asserts:
            Letting count equals 1.
            Letting title equals 'Location'.
        """
        address = Address.objects.create(
            number=1,
            street='Main Street',
            city='New York',
            state='NY',
            zip_code=10001,
            country_iso_code='USA'
        )
        letting = Letting.objects.create(title='Location', address=address)
        self.assertEqual(Letting.objects.count(), 1)
        self.assertEqual(letting.title, 'Location')

    def test_letting_str(self):
        """Test that letting string representation returns title.

        Creates a letting and verifies its __str__ method returns
        the letting's title.

        Asserts:
            String representation equals 'Beautiful Apartment'.
        """
        address = Address.objects.create(
            number=1,
            street='Main Street',
            city='New York',
            state='NY',
            zip_code=10001,
            country_iso_code='USA'
        )
        letting = Letting.objects.create(title='Beautiful Apartment', address=address)
        self.assertEqual(str(letting), 'Beautiful Apartment')
