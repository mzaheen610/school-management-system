"""
Views for user login/logout.
"""

from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from user.forms import LoginForm


def index(request):
    """View for the home page."""
    return render(request, 'index.html')


def login_page_view(request):
    """View for the login page."""
    messages_data = messages.get_messages(request)
    print(messages_data)
    return render(request, 'login.html', {'form': LoginForm(), 'messages': messages_data})


def login_view(request):
    """View for logging in the user."""

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('home')  # Redirect to your home page or any other page
            else:
                messages.error(request, 'Invalid email or password.')
    else:
        # Handle the case where the user tries to access the login view directly without submitting the form.
        messages.warning(request, 'Please submit the login form.')

    return redirect('login_form')  # Redirect back to the login form


def logout_view(request):
    """View to handle logout"""

    logout(request)

    return redirect('home')