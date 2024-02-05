from calendar import FRIDAY, MONDAY, SATURDAY, SUNDAY, THURSDAY, TUESDAY, WEDNESDAY
from random import choices
from django.db import models
from core.models import Staff
from django.core.validators import MinValueValidator, MaxValueValidator
from enum import Enum


class Subject(models.Model):
    subject_id = models.IntegerField(primary_key=True)
    subject_name = models.CharField(max_length=255)


class Teachers(models.Model):
    teacher_id = models.IntegerField(primary_key=True)
    staff = models.OneToOneField(Staff, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,  null=False, blank=False, on_delete=models.CASCADE)


class StandardEnum:
    first = 'I'
    second = 'II'
    third = 'III'
    fourth = 'IV'
    fifth = 'V'
    sixth = 'VI'
    seventh = "VII"
    eight = "VIII"

    CHOICES = [
        (first, 'I'),
        (second, 'II'),
        (third, 'III'),
        (fourth, 'IV'),
        (fifth, 'V'),
        (sixth, 'VI'),
        (seventh, 'VII'),
        (eight,'VIII')
    ]


class Class(models.Model):
    class_id = models.IntegerField(primary_key=True)
    class_teacher = models.OneToOneField(Teachers, on_delete=models.CASCADE)
    standard = models.CharField(max_length=255, choices=StandardEnum.CHOICES)
    capacity = models.IntegerField()
    room_no = models.IntegerField()


class WeekDayEnum:
    MON = 'Monday'
    TUE = 'Tuesday'
    WED = 'Wednesday'
    THU = 'Thursday'
    FRI = 'Friday'
    SAT = 'Saturday'
    SUN = 'Sunday'

    CHOICES = [
        (MON, 'Monday'),
        (TUE, 'Tuesday'),
        (WED, 'Wednesday'),
        (THU, 'Thursday'),
        (FRI, 'Friday'),
        (SAT, 'Saturday'),
        (SUN, 'Sunday'),
    ]


class ClassSchedules(models.Model):
    schedule_id = models.IntegerField(primary_key=True)
    classroom = models.ForeignKey(Class, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=255, choices=WeekDayEnum.CHOICES)
    slot = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(6)
        ]
    )
    subject_id = models.ForeignKey(Subject , on_delete=models.CASCADE)