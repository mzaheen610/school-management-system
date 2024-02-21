"""
Forms for user login.
"""

from django import forms


class LoginForm(forms.Form):
    """Login form"""
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
