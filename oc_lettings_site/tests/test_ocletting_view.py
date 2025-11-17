"""Tests for ocletting views.

This module contains tests for the oc core application views.
"""
from django.urls import reverse
from django.test import TestCase


class TestLettingViews(TestCase):
    """Test cases for ocletting-related views."""

    def test_ocletting_index(self):
        """Test that oclettings index page returns 200 and uses correct template."""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
