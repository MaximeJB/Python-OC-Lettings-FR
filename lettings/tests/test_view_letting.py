"""Tests for letting views.

This module contains tests for the lettings application views.
"""
from django.urls import reverse
from django.test import TestCase

from lettings.models import Address, Letting


class TestLettingViews(TestCase):
    """Test cases for letting-related views."""

    def test_letting_index(self):
        """Test that lettings index page returns 200 and uses correct template.

        Makes a GET request to the lettings index page and verifies
        the response status and template used.

        Asserts:
            Response status code equals 200.
            Template used is 'lettings/index.html'.
        """
        response = self.client.get(reverse('lettings:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/index.html')

    def test_letting_detail(self):
        """Test that letting detail page returns 200 and uses correct template.

        Creates a letting with an address, makes a GET request to the
        letting detail page, and verifies response status and template.

        Asserts:
            Template used is 'lettings/letting.html'.
            Response status code equals 200.
        """
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
        response = self.client.get(reverse('lettings:letting', args=[letting.id]))
        self.assertTemplateUsed(response, 'lettings/letting.html')
        self.assertEqual(response.status_code, 200)

    def test_letting_detail_not_found(self):
        """Test that letting detail page returns 404 for non-existent letting.

        Makes a GET request to a letting detail page with an ID that
        doesn't exist and verifies a 404 response is returned.

        Asserts:
            Response status code equals 404.
        """
        response = self.client.get(reverse('lettings:letting', args=[9999]))
        self.assertEqual(response.status_code, 404)
