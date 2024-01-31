"""
Serializers for the Student API.
"""

from rest_framework import serializers
from core.models import Student


class StudentSerializer(serializers.ModelSerializer):
    """Serializer for the student model."""
    class Meta:
        model = Student
        fields = ['id', 'name', 'student_id', 'date_of_birth', 'join_date', 'current_class', 'email']
        read_only_fields = ['id']

