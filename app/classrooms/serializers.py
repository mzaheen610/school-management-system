from rest_framework import serializers
from classrooms.models import Teachers, Class, Subject

class TeacherSerializer(serializers.ModelSerializer):
    """Serilizer for teacher model"""

    class Meta:
        model = Teachers
        fields = ['teacher_id','staff_id']
        # read_only_fields = ['teacher_id']

class TeacherCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating teacher obj"""\
    
    class Meta:
        model = Teachers
        fields = ['staff_id']