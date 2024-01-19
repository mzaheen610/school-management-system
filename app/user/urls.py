"""
Urls for user login and logout.
"""
from django.urls import path
from user import views

urlpatterns = [
    path('', views.index, name='home'),
]