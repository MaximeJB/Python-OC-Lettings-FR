"""Tests for ocletting views.

This module contains tests for the oc core application views.
"""
from django.urls import reverse
from django.test import TestCase, RequestFactory

from oc_lettings_site.views import custom_404, custom_500


class TestLettingViews(TestCase):
    """Test cases for ocletting-related views."""

    def test_ocletting_index(self):
        """Test that oclettings index page returns 200 and uses correct template.

        Makes a GET request to the main homepage and verifies
        the response status and template used.

        Asserts:
            Response status code equals 200.
            Template used is 'index.html'.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_custom_404(self):
        """Test that custom 404 handler returns 404 status.

        Creates a mock request and calls the custom_404 handler directly,
        verifying it returns the correct status code.

        Asserts:
            Response status code equals 404.
        """
        factory = RequestFactory()
        request = factory.get('/nonexistent-page/')
        response = custom_404(request, exception=Exception("Page not found"))
        self.assertEqual(response.status_code, 404)

    def test_custom_500(self):
        """Test that custom 500 handler returns 500 status.

        Creates a mock request and calls the custom_500 handler directly,
        verifying it returns the correct status code.

        Asserts:
            Response status code equals 500.
        """
        factory = RequestFactory()
        request = factory.get('/error/')
        response = custom_500(request)
        self.assertEqual(response.status_code, 500)
