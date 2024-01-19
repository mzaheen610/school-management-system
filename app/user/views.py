"""
Views for user login/logout.
"""

from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseBadRequest

def index(request):
    """View for the home page."""
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # if user.user_type == 'admin':
            #     return redirect('admin:index')
            # elif user.user_type == 'staff':
            #     return redirect('staff_dashboard')
            # elif user.user_type == 'parent':
            #     return redirect('parent_dashboard')
        else:
            return HttpResponseBadRequest('Invalid login credentials')

    return HttpResponseBadRequest('Invalid request method')