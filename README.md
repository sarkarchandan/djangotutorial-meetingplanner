# Django tutorial project - Meeting Planner
---

## Django project structure
---

A Django project is a big python package, which typically contains models, views, templates, and urls among others. A 
Django project also contains several `apps`, each of them itself is another child package of the main Django project 
package. It is a convention in the Django project to distribute the functionalities of the web application in to these 
smaller `apps`. In more advanced use cases, these `apps` can be reused by multiple Django projects, which is out of 
scope for this beginner project. Each of these `apps` should be small, easily defined unit of work, contributing to the 
main web application.

## Useful commands:
---

* `django-admin startproject meeting_planner` - To start a django project called meeting_planner.
* `python meeting_planner/manage.py runserver` - To start the django web server for the meeting_planner project in its 
initial form.

> Django by default runs the server in the debug mode i.e., in the `meeting_planner/meeting_planner/settings.py`,
> `DEBUG = True`. This is not advisable, when the app is deployed in the production.

> The `meeting_planner/meeting_planner/settings.py` file in this project encapsulates all the server settings for the 
> meeting_planner web application. For example, we change the `LANGUAGE_CODE` or `TIME_ZONE` used in the project.

## Files created by the startproject command and their purposes:
---

* `meeting_planner/manage.py` - Entry point for the project, which dispatches the commands like _runserver_ and 
_manage_ etc.
* `meeting_planner/db.sqlite3` - Created upon running the server to store the data models as relational tables.
* `meeting_planner/meeting_planner/asgi.py` - Needed for project deployment to production.
* `meeting_planner/meeting_planner/wsgi.py` - Needed for project deployment to production.
* `meeting_planner/meeting_planner/settings.py` - Customizes the project as per our needs.
* `meeting_planner/meeting_planner/urls.py` - Registers routes to the webserver.

## Phase I:
* Create a Django app.
  * `python manage.py startapp website` - Creates an app called `website` inside the `meeting_planner` directory. It is
    a convention in Django to manage the parent web application in smaller set of units called **apps**. An app is 
    basically a Python package. This is supposed to create a file structure with the root directory name as `website` 
    inside the parent `meeting_planner` directory. For now, we'd remove everything, what were created leaving only 
    `__init__.py` and `views.py`. We'd do so to understand, what an **app** is, and how it fits inside a Django web 
    application.
    * Add the `website` in the list `INSTALLED_APPS` inside the `meeting_planner/meeting_planner/settings.py`, because 
      meeting_planner is the main Django web application, which we are building.
    * We go to the website app, and create a **view** inside the views.py. A view in Django handles the request to a web 
      page. In order to make simple page come into existence, we perform the following steps.
      * Add a handler function e.g., `welcome(request: HttpRequest) -> HttpResponse` to the `website/views.py`.
      * Register a path in the `meeting_planner/urls.py` in the `urlpatterns` list as `path('welcome.html', welcome)`, 
        which adds a path string _welcome.html_ and registers `welcome` function as the respective handler of the 
        request received in this path. And then upon running the server, the path is served.
      * We also can register the handler function for the homepage in the same way, where we'd register the path to be 
        something like `path('', home)`.
* Add a view function.
* Assign an url to the view function.
* Run and view the page.