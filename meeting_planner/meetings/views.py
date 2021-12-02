from typing import Union, List
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Meeting, Room
from django.http import HttpRequest, HttpResponse


# Create your views here.
def meeting_detail(request: HttpRequest, meeting_id: int) -> HttpResponse:
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


def rooms(request: HttpRequest) -> HttpResponse:
    """Implements the view handler function for displaying
    all rooms.

    Args:
        request(HttpRequest): Incoming request to the
        rooms page.

    Returns:
        HttpResponse: Outgoing response to the browser.
    """
    rms: Union[List[Room], None] = get_list_or_404(klass=Room)
    return render(request=request, template_name='rooms/all.html', context={
        'rooms': rms,
    })


def room_detail(request: HttpRequest, room_id: int) -> HttpResponse:
    """Implements the view handler function for displaying
    room detail.

    Args:
        request (HttpRequest): Incoming request to the
            room detail page.
        room_id (int): Identifier for a room.

    Returns:
        HttResponse: Outgoing response to the browser.
    """
    room: Union[Room, None] = get_object_or_404(klass=Room, pk=room_id)
    return render(request=request, template_name='rooms/detail.html', context={
        'room': room,
    })
