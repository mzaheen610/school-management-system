import random
from urllib import request
from django.shortcuts import render
# Create your views here.
from classrooms.serializers import TeacherSerializer, TeacherCreateSerializer
from rest_framework import (
    viewsets,
    generics
    )
from classrooms.models import Teachers


class ListTeacherView(generics.ListAPIView):
    serializer_class = TeacherSerializer
    queryset = Teachers.objects.all()

class CreateTeacherView(generics.CreateAPIView):
    serializer_class = TeacherCreateSerializer
    queryset = Teachers.objects.all()

    def perform_create(self, serializer):
        last_id =  self.queryset.order_by('-teacher_id')[0].teacher_id +1 if self.queryset.count() > 0 else 1
        # teacher_number = 't' + str(last_id).zfill(8)
        teacher_number = "{:0>8}".format(str(last_id))
        serializer.save(teacher_id=teacher_number)


class UpdateTeacherView(generics.UpdateAPIView):
    serializer_class = TeacherSerializer
    queryset = Teachers.objects.all()
    lookup_field = 'teacher_id'

class DeleteTeacherView(generics.DestroyAPIView):
    serializer_class = TeacherSerializer
    queryset = Teachers.objects.all()
    lookup_field = 'teacher_id'
