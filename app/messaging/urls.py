"""
Urls for the messaging system.
"""

from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.messagingHomePage, name="message"),
]