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
    return HttpResponse(f'<h1>Welcome to the meeting planner. Time now is: {datetime.datetime.now()}</h1>')


def home(request: HttpRequest) -> HttpResponse:
    """Serves as the handler of the home page for the meeting planner website. Acts as a view function for the
    website app.

    Phase I: We return a simple HTTPResponse object
    Phase III: We return HTTPResponse object, which uses a rendering template.

    Args:
         request (HttpRequest): Incoming request to the home page.

    Returns:
         HttpResponse: Outgoing response to the browser.
    """
    # NOTE: context parameter adds a dictionary of values to the template context. These values can be used inside
    # the Jinja syntax.
    # NOTE: Reference: https://docs.djangoproject.com/en/3.2/topics/http/shortcuts/#render
    return render(request=request, template_name='website/welcome.html', context={
        'name': 'Meeting Planner',
        'author': 'Reindert-Jan Ekker',
        'message': 'Sample message, would be updated later',
    })
