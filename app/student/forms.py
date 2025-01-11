"""
Forms for student enrollment.
"""

from django import forms

class StudentEnrollmentForm(forms.Form):
    """Enrollment form"""
    name = forms.CharField()
    date_of_birth = forms.DateField()
    current_class = forms.CharField()
    email = forms.EmailField()
