"""Tests for Address and Letting models.

This module contains tests for the Address and Letting models
in the lettings application.
"""
from django.test import TestCase
from lettings.models import Letting, Address


class AddressModelTest(TestCase):
    """Test cases for the Address model."""

    def test_create_address(self):
        """Test that an address can be created and saved correctly."""
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
        """Test that address string representation returns number and street."""
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
        """Test that a letting can be created with an address."""
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
        """Test that letting string representation returns title."""
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
