"""
Urls for the dashboard app.
"""

from django.urls import path
from .views import dashboardView

urlpatterns = [
    path('sample/', dashboardView, name ="sample-dashboard" )
]
