import random
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from yaml import serialize
from rest_framework import status
from rest_framework.response import Response
from classrooms.serializers import (
    TeacherSerializer, 
    TeacherCreateSerializer, 
    SubjectSerializer, 
    SubjectCreateSerializer,
    ClassSerializer,
    ClassCreateSerializer,
    ClassSchedulesSerializer,
    ClassSchedulesCreateSerializer,
    CreateDaySchedule
    )
from rest_framework import (
    viewsets,
    generics
    )
from classrooms.models import (
    Teachers, 
    Subject,
    Class,
    ClassSchedules
    )


class ListTeacherView(generics.ListAPIView):
    serializer_class = TeacherSerializer
    queryset = Teachers.objects.all()

    def list(self, request, *args, **kwargs):
        if self.request.user.is_staff: # type: ignore
            return super().list(request, *args, **kwargs)
        else:
            return HttpResponse("You are not authorized to view this.")


class CreateTeacherView(generics.CreateAPIView):
    serializer_class = TeacherCreateSerializer
    queryset = Teachers.objects.all()

    def create(self, request, *args, **kwargs):
            if self.request.user.is_staff: # type: ignore
                return super().create(request, *args, **kwargs)
            else:
                return HttpResponse("You are not authorized.")
            
    def perform_create(self, serializer):
        last_id =  self.queryset.order_by('-teacher_id')[0].teacher_id +1 if self.queryset.count() > 0 else 1
        # teacher_number = 't' + str(last_id).zfill(8)
        teacher_number = "{:0>8}".format(str(last_id))
        serializer.save(teacher_id=teacher_number)
    

class UpdateTeacherView(generics.UpdateAPIView):
    serializer_class = TeacherSerializer
    queryset = Teachers.objects.all()
    lookup_field = 'teacher_id'

    def update(self, request, *args, **kwargs):
        if self.request.user.is_staff: # type: ignore
            return super().update(request,*args,**kwargs)
        else:
            return HttpResponse("You are not authorized.")


class DeleteTeacherView(generics.DestroyAPIView):
    serializer_class = TeacherSerializer
    queryset = Teachers.objects.all()
    lookup_field = 'teacher_id'

    def delete(self, request, *args, **kwargs):
        if self.request.user.is_staff: # type: ignore
            return super().delete(request,*args,**kwargs)
        else:
            return HttpResponse("you are not authorized")


class CreateSubjectView(generics.CreateAPIView):
    serializer_class = SubjectCreateSerializer
    queryset = Subject.objects.all()

    def create(self, request, *args, **kwargs):
        if self.request.user.is_staff: # type: ignore
                return super().create(request, *args, **kwargs)
        else:
            return HttpResponse("Not authorized")
        
    def perform_create(self, serializer):
        last_subject_id = Subject.objects.all().order_by('-subject_id')[0].subject_id+1 if self.queryset.count() > 0 else 1
        subject_code = str(last_subject_id).zfill(3)
        serializer.save(subject_id=subject_code)


class ListSubjectView(generics.ListAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    lookup_field = 'subject_id'

    def list(self, request, *args, **kwargs):
        if self.request.user.is_staff: # type: ignore
            return super().list(request,*args,**kwargs)
        else:
            return HttpResponse("You are not authorized.")


class updateSubjectView(generics.UpdateAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    lookup_field = 'subject_id'

    def update(self, request, *args, **kwargs):
        if self.request.user.is_staff: # type: ignore
            return super().update(request,*args,**kwargs)
        else:
            return HttpResponse("You are not authorized.")


class DeleteSubjectView(generics.DestroyAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    lookup_field = 'subject_id'

    def delete(self, request, *args, **kwargs):
        if self.request.user.is_staff: # type: ignore
            return super().delete(request,*args,**kwargs)
        else:
            return HttpResponse("You are not authorized.")
        

class CreateClassView(generics.CreateAPIView):
    serializer_class = ClassCreateSerializer
    queryset = Class.objects.all()

    def create(self, request, *args, **kwargs):
        if self.request.user.is_staff: # type: ignore
                return super().create(request, *args, **kwargs)
        else:
            return HttpResponse("Not authorized")
        
    def perform_create(self, serializer):
        last_Class_id = Class.objects.all().order_by('-Class_id')[0].class_id+1 if self.queryset.count() > 0 else 1
        class_code = str(last_Class_id).zfill(3)
        serializer.save(class_id=class_code)


class ListClassView(generics.ListAPIView):
    serializer_class = ClassSerializer
    queryset = Class.objects.all()
    lookup_field = 'Class_id'

    def list(self, request, *args, **kwargs):
        if self.request.user.is_staff: # type: ignore
            return super().list(request,*args,**kwargs)
        else:
            return HttpResponse("You are not authorized.")


class updateClassView(generics.UpdateAPIView):
    serializer_class = ClassSerializer
    queryset = Class.objects.all()
    lookup_field = 'Class_id'

    def update(self, request, *args, **kwargs):
        if self.request.user.is_staff: # type: ignore
            return super().update(request,*args,**kwargs)
        else:
            return HttpResponse("You are not authorized.")


class DeleteClassView(generics.DestroyAPIView):
    serializer_class = ClassSerializer
    queryset = Class.objects.all()
    lookup_field = 'Class_id'

    def delete(self, request, *args, **kwargs):
        if self.request.user.is_staff: # type: ignore
            return super().delete(request,*args,**kwargs)
        else:
            return HttpResponse("You are not authorized.")
        

class CreateClassSchedulesView(generics.CreateAPIView):
    serializer_class = ClassSchedulesCreateSerializer
    queryset = ClassSchedules.objects.all()

    def create(self, request, *args, **kwargs):
        if self.request.user.is_staff: # type: ignore
                return super().create(request, *args, **kwargs)
        else:
            return HttpResponse("Not authorized")
        
    def perform_create(self, serializer):
        classSchedules_id = ClassSchedules.objects.all().order_by('-schedule_id')[0].schedule_id+1 if self.queryset.count() > 0 else 1
        classSchedules_code = str(classSchedules_id).zfill(3)
        serializer.save(schedule_id=classSchedules_code)


class ListClassSchedulesView(generics.ListAPIView):
    serializer_class = ClassSchedulesSerializer
    queryset = ClassSchedules.objects.all()
    lookup_field = 'ClassSchedules_id'

    def list(self, request, *args, **kwargs):
        if self.request.user.is_staff: # type: ignore
            return super().list(request,*args,**kwargs)
        else:
            return HttpResponse("You are not authorized.")


class UpdateClassSchedulesView(generics.UpdateAPIView):
    serializer_class = ClassSchedulesSerializer
    queryset = ClassSchedules.objects.all()
    lookup_field = 'ClassSchedules_id'

    def update(self, request, *args, **kwargs):
        if self.request.user.is_staff: # type: ignore
            return super().update(request,*args,**kwargs)
        else:
            return HttpResponse("You are not authorized.")


class DeleteClassSchedulesView(generics.DestroyAPIView):
    serializer_class = ClassSchedulesSerializer
    queryset = ClassSchedules.objects.all()
    lookup_field = 'ClassSchedules_id'

    def delete(self, request, *args, **kwargs):
        if self.request.user.is_staff: # type: ignore
            return super().delete(request,*args,**kwargs)
        else:
            return HttpResponse("You are not authorized.")
        

class CreateDayScheduleView(generics.CreateAPIView):
    serializer_class = CreateDaySchedule
    
    def create(self, request, *args, **kwargs):
        if self.request.user.is_staff: # type: ignore
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                day = serializer.validated_data['day']
                classid = serializer.validated_data['class_id']
                slots = [serializer.validated_data[f'slot{i+1}'] for i in range(6)]
                class_obj = Class.objects.get(class_id=classid)
                for i, sub in enumerate(slots):
                    subject = Subject.objects.get(subject_id=sub)

                    last_classSchedules_id = ClassSchedules.objects.all().order_by('-schedule_id')[0].schedule_id+1 if ClassSchedules.objects.count() > 0 else 1
                    classSchedules_code = str(last_classSchedules_id).zfill(3)

                    ClassSchedules.objects.create(schedule_id = classSchedules_code, day_of_week=day, classroom=class_obj, slot=i+1, subject_id=subject )
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)