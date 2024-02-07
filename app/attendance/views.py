"""
Views for the attendance API.
"""

from rest_framework import viewsets, mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpResponse
from .serializers import StudentAttendanceSerializer
from .models import StudentAttendance, StaffAttendance


class StudentAttendanceView(viewsets.GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin):
    """View for marking attendance of students."""

    queryset = StudentAttendance.objects.all()
    serializer_class = StudentAttendanceSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        if self.request.user.is_parent or self.request.user.is_school_staff:
            return HttpResponse("You are not authorized to view this.")

        student_id = request.query_params.get('student_id')
        attendance_date = request.query_params.get('attendance_date')
        if student_id:
            queryset = self.get_queryset().filter(student=student_id)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        elif attendance_date:
            queryset = self.get_queryset().filter(date=attendance_date)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        elif student_id and attendance_date:
            queryset = self.get_queryset().filter(student=student_id, date=attendance_date)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)


        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        if self.request.user.is_parent:
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


def StudentAttendancePageView(request):
    """View for marking student attendance."""
    return render(request, 'mark_student_attendance.html')

