from django.urls import path
from .views import team_view

urlpatterns = [
    path('team/', team_view, name='team-home'),
]
