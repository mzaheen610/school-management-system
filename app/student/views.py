"""
Views for the student API.
"""

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from .serializers import StudentSerializer
from .permissions import IsAdmin, IsSchoolStaff, IsParent
from core.models import Student

class StudentAPIView(viewsets.ModelViewSet):
    """Viewset for viewing and managing student profiles."""

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdmin]

    def get_permissions(self):
        if self.action == 'list':
            return [IsAdmin() or IsSchoolStaff()]
        elif self.action == 'retrieve':
            print("Here")
            return [IsAdmin() or IsSchoolStaff() or IsParent()]
        elif self.action in ['update', 'partial_update']:
            return [IsAdmin() or IsSchoolStaff()]
        else:
            return super().get_permissions()
