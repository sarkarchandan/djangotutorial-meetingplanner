# Django tutorial project - Meeting Planner
---

## Useful commands:

* `django-admin startproject meeting_planner` - To start a django project called meeting_planner.
* `python meeting_planner/manage.py runserver` - To start the django web server for the meeting_planner project in its 
initial form.

## Files created by the startproject command and their purposes:
* `meeting_planner/manage.py` - Entry point for the project, which dispatches the commands like __runserver__ and 
__manage__ etc.
* `meeting_planner/db.sqlite3` - Created upon running the server to store the data models as relational tables.
* `meeting_planner/meeting_planner/asgi.py` - Needed for project deployment to production.
* `meeting_planner/meeting_planner/wsgi.py` - Needed for project deployment to production.
* `meeting_planner/meeting_planner/settings.py` - Customizes the project as per our needs.
* `meeting_planner/meeting_planner/urls.py` - Registers routes to the webserver.
