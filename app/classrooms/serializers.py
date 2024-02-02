from pyexpat import model
from unittest.util import _MAX_LENGTH
from attr import fields
from rest_framework import serializers
from classrooms.models import ClassSchedules, Teachers, Class, Subject

class TeacherSerializer(serializers.ModelSerializer):
    """Serilizer for teacher model"""

    class Meta:
        model = Teachers
        fields = ['teacher_id', 'staff', 'subject']
        # read_only_fields = ['teacher_id']

class TeacherCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating teacher obj"""
    
    class Meta:
        model = Teachers
        fields = ['staff','subject']

class SubjectSerializer(serializers.ModelSerializer):
    """Serializer for subject model"""

    class Meta:
        model = Subject
        fields = ["subject_id","subject_name"]
    
class SubjectCreateSerializer(serializers.ModelSerializer):
    """Serializer for subject model"""

    class Meta:
        model = Subject
        fields = ["subject_name"]


class ClassSerializer(serializers.ModelSerializer):
    """Serializer for class model."""

    class Meta: 
        model = Class
        fields = ["class_id", "class_teacher", "standard", "capacity", "room_no"]


class  ClassCreateSerializer(serializers.ModelSerializer):
    """Serializer for the class model."""
     
    class Meta:
        model = Class
        fields = ["class_teacher", "standard", "capacity", "room_no"]


class ClassSchedulesSerializer(serializers.ModelSerializer):
    """Serializer for class model."""

    class Meta: 
        model = ClassSchedules
        fields = ["schedule_id", "classroom", "day_of_week", "slot", "subject_id"]


class ClassSchedulesCreateSerializer(serializers.ModelSerializer):
    """Serializer for the class model."""
     
    class Meta:
        model = ClassSchedules
        fields = ["classroom", "day_of_week", "slot", "subject_id"]


class CreateDaySchedule(serializers.Serializer):

    day = serializers.CharField(required=True)
    class_id = serializers.IntegerField(required=True)
    slot1 = serializers.IntegerField(required=True)
    slot2 = serializers.IntegerField(required=True)
    slot3 = serializers.IntegerField(required=True)
    slot4 = serializers.IntegerField(required=True)
    slot5 = serializers.IntegerField(required=True)
    slot6 = serializers.IntegerField(required=True)


