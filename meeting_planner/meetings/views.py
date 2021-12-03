from typing import Union, List, Type
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .forms import MeetingForm
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


def new_meeting(request: HttpRequest) -> HttpResponse:
    """Implements the view handler function for
    displaying new meeting form

    Args:
        request(HttpRequest): Incoming request to
            the new meeting path.

    Returns:
        HttpResponse: Outgoing response to the
            browser.
    """
    if request.method == 'POST':
        # Retrieve and process data
        form: MeetingForm = MeetingForm(data=request.POST)
        if form.is_valid():
            form.save()
            # This is a special method, because in the 'to' argument we
            # are actually passing the name of a view function, for
            # which the url should be retrieved and redirected to.
            return redirect(to='home')
    else:  # GET
        form: MeetingForm = MeetingForm()
    # Returns the form template in two cases, 1) the form submission
    # was invalid 2) the request to the view function was GET, which
    # means user to be presented with the form.
    return render(request=request, template_name='meetings/new.html', context={
        'form': form
    })

