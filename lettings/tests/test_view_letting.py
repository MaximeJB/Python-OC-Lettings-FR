"""Tests for letting views.

This module contains tests for the lettings application views.
"""
from django.urls import reverse
from django.test import TestCase

from lettings.models import Address, Letting


class TestLettingViews(TestCase):
    """Test cases for letting-related views."""

    def test_letting_index(self):
        """Test that lettings index page returns 200 and uses correct template."""
        response = self.client.get(reverse('lettings_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/lettings_index.html')

    def test_letting_detail(self):
        """Test that letting detail page returns 200 and uses correct template."""
        letting = Letting.objects.create(
            title='Paris',
            address=Address.objects.create(
                id=1,
                number=1,
                street='2',
                city='Paris',
                state='Fr',
                zip_code=86000,
                country_iso_code='111'
            )
        )
        response = self.client.get(reverse('letting', args=[letting.id]))
        self.assertTemplateUsed(response, 'lettings/letting.html')
        self.assertEqual(response.status_code, 200)
