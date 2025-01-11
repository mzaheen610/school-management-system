"""
Urls for the dashboard app.
"""

from django.urls import path
from .views import dashboardView, attendanceDataView

urlpatterns = [
    path('sample/', dashboardView, name ="sample-dashboard" ),
    path('api/attendance/', attendanceDataView, name="attendance-data-api")
]
