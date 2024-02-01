from django.db import models
from core.models import Staff


class Subject(models.Model):
    subject_id = models.IntegerField(primary_key=True)
    subject_name = models.CharField(max_length=255)


class Teachers(models.Model):
    teacher_id = models.IntegerField(primary_key=True)
    staff_id = models.OneToOneField(Staff, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject,  null=False, blank=False, on_delete=models.CASCADE)

class ClassSchedules(models.Model):
    schedule_id = models.IntegerField(primary_key=True)
    class_id = models.ForeignKey('Class', on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=20)
    time_start = models.TimeField()
    time_end = models.TimeField()
    subject_id = models.ForeignKey('Subject', on_delete=models.CASCADE)

class Class(models.Model):
    class_id = models.IntegerField(primary_key=True)
    standard = models.CharField(max_length=255)
    capacity = models.IntegerField()
    room_no = models.IntegerField()
