from typing import Union
from django.shortcuts import render, get_object_or_404
from .models import Meeting
from django.http import HttpRequest, HttpResponse


# Create your views here.
def detail(request: HttpRequest, meeting_id: int) -> HttpResponse:
    """Implements the view handler function for displaying
    meeting detail.

    Args:
        request (HttpRequest): Incoming request to the
        meeting detail page.
        meeting_id (int): Identifier for a meeting

    Returns:
        HttpResponse: Outgoing response to the browser.
    """
    meeting: Union[Meeting, None] = get_object_or_404(klass=Meeting, pk=meeting_id)
    return render(request=request, template_name='meetings/detail.html', context={
        'meeting': meeting,
    })
