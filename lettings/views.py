"""Views for the lettings application.

This module contains views to display lettings list and individual letting details.
"""
import logging
from django.shortcuts import render
from django.http import Http404
from .models import Letting

logger = logging.getLogger(__name__)


def index(request):
    """Display list of all lettings.

    Args:
        request: HTTP request object.

    Returns:
        HttpResponse: Rendered template with list of lettings.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    logger.info("Lettings index page accessed")
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """Display details of a specific letting.

    Args:
        request: HTTP request object.
        letting_id: Primary key of the letting.

    Returns:
        HttpResponse: Rendered template with letting details.

    Raises:
        Http404: If letting with given id does not exist.
    """
    try:
        letting = Letting.objects.get(id=letting_id)
        logger.info(f"Letting {letting_id} accessed successfully")
    except Letting.DoesNotExist:
        logger.error(f"Letting with id {letting_id} not found")
        raise Http404("Letting not found")
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
