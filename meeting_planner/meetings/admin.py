from django.contrib import admin
from meetings.models import Meeting, Room

# Register your models here.
admin.site.register(Meeting)  # Registers the Meeting model with the Django admin site
admin.site.register(Room)  # Registers the Room model with the Django admin site
