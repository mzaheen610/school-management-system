"""
Views for the student API and student management.
"""
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import StudentSerializer
from . import forms
from core.models import Student


class StudentAPIView(viewsets.GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.CreateModelMixin):
    """Viewset for viewing and managing student profiles."""

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes= [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        if self.request.user.is_parent:
            return HttpResponse("You are not authorized to view this.")
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        if self.request.user.is_parent or self.request.user.is_school_staff:
            return HttpResponse("You are not authorized to view this.")
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if self.request.user.is_parent or self.request.user.is_school_staff:
            return HttpResponse("You are not authorized to view this.")
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if self.request.user.is_parent or self.request.user.is_school_staff:
            return HttpResponse("You are not authorized to view this.")
        return super().destroy(request, *args, **kwargs)


    @action(detail=False, methods=['get'], url_path='class', url_name='fetch-student-by-class')
    def fetch_students_by_class(self, request):
        """Query students in a class."""
        if self.request.user.is_parent:
            return HttpResponse("You are not authorized to view this.")
        class_id = request.query_params.get('class_id')
        if class_id:
            # Filter students based on class_id
            queryset = self.queryset.filter(current_class=class_id)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({"detail": "class_id parameter is required."}, status=400)


def StudentEnrollmentPageView(request):
    """View for student enrollment page."""
    return render(request, 'enroll_student.html', {'form': forms.StudentEnrollmentForm()})


# def StudentEnrollmentView(request):
#     """View for student enrollment."""
#     if request.method == 'POST':

def StudentProfileView(request):
    """View for the student profile page."""
    return render(request, 'student_profile.html')