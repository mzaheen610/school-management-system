"""
Serializers for the attendance API.
"""

from rest_framework import serializers
from .models import StudentAttendance, StaffAttendance


class StaffAttendanceSerializer(serializers.ModelSerializer):
    """Serializer for the staff attendance api"""
    class Meta:
        model = StaffAttendance
        fields = ['staff', 'date', 'status', 'comment']


class StudentAttendanceSerializer(serializers.ModelSerializer):
    """Serializer for the student attendance api"""
    class Meta:
        model = StudentAttendance
        fields = ['student', 'date', 'status', 'comment']
