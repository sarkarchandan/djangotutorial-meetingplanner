from django.urls import path
from .views import rooms, room_detail, meeting_detail, new_meeting


urlpatterns = [
    # Include url mapping with an integer path parameter
    path('<int:meeting_id>', meeting_detail, name='meeting_detail'),
    path('rooms', rooms, name='rooms'),
    path('rooms/<int:room_id>', room_detail, name='room_detail'),
    path('new_meeting', new_meeting, name='new_meeting'),
]
