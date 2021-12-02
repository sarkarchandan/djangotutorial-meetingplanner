"""meeting_planner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from website.views import welcome, home
from meetings.views import meeting_detail, room_detail, rooms


urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome', welcome, name='welcome'),
    path('', home, name='home'),
    # Include url mapping with an integer path parameter
    path('meetings/<int:meeting_id>', meeting_detail, name='meeting_detail'),
    path('rooms', rooms, name='rooms'),
    path('rooms/<int:room_id>', room_detail, name='room_detail'),
]
