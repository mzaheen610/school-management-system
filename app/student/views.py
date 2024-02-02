"""
Views for the student API.
"""
from re import X
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import StudentSerializer
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