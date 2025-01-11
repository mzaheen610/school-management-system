"""
Views for the messaging app.
"""
from django.shortcuts import render

def messagingHomePage(request):
    return render(request, 'lobby.html')
