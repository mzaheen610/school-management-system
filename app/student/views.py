"""
Views for the student API.
"""

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from student.serializers import StudentSerializer
from core.models import Student

class StudentAPIView(viewsets.ModelViewSet):
    """Viewset for viewing and managing student profiles."""

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
