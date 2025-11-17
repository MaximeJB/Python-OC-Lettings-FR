"""Views for the main oc_lettings_site application.

This module contains the main homepage view and custom error handlers.
"""
from django.shortcuts import render


def index(request):
    """Display the homepage of the site.

    Args:
        request: HTTP request object.

    Returns:
        HttpResponse: Rendered homepage template.
    """
    return render(request, 'index.html')


def custom_404(request, exception):
    """Display custom 404 error page.

    Args:
        request: HTTP request object.
        exception: The exception that triggered the 404.

    Returns:
        HttpResponse: Rendered 404 error template with status 404.
    """
    return render(request, '404.html', status=404)


def custom_500(request):
    """Display custom 500 error page.

    Args:
        request: HTTP request object.

    Returns:
        HttpResponse: Rendered 500 error template with status 500.
    """
    return render(request, '500.html', status=500)
