from django.db import models
from datetime import time


# Create your models here.
class Room(models.Model):
    """Model class for the room table"""
    name: models.CharField = models.CharField(max_length=50)
    floor_number: models.IntegerField = models.IntegerField(default=0)
    room_number: models.IntegerField = models.IntegerField(default=1)

    def __str__(self) -> str:
        """Creates a string representation. This would be handy
        for better display of the objects in the UI.

        Returns:
             str: String representation
        """
        return f'{self.name} with room number {self.room_number} at {self.floor_number} floor'


class Meeting(models.Model):
    """Model class for the meeting table. Django would look at the class attributes and create the __init__ method
    for the class for us."""
    title: models.CharField = models.CharField(max_length=200)
    date: models.DateField = models.DateField()
    start_time: models.TimeField = models.TimeField(default=time(9))
    duration: models.IntegerField = models.IntegerField(default=1)
    room: models.ForeignKey = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self) -> str:
        """Creates a string representation. This would be handy
        for better display of the objects in the UI.

        Returns:
            str: String representation.
        """
        return f'{self.title} at {self.start_time} on {self.date}'




