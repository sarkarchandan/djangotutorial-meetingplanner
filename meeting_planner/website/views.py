import datetime
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.
def welcome(request: HttpRequest) -> HttpResponse:
    """Serves as the handler of the welcome page for the meeting planner website. Acts as a view function for the
    website app.

    Args:
         request (HttpRequest): Incoming request to the welcome page.

    Returns:
         HttpResponse: Outgoing response to the browser.
    """
    return HttpResponse('Welcome to the meeting planner')


def home(request: HttpRequest) -> HttpResponse:
    """Serves as the handler of the home page for the meeting planner website. Acts as a view function for the
    website app.

    Args:
         request (HttpRequest): Incoming request to the home page.

    Returns:
         HttpResponse: Outgoing response to the browser.
    """
    return HttpResponse(f'<h1>Welcome to the meeting planner. Time now is: {datetime.datetime.now()}</h1>')
