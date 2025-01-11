"""
Models for the attendance API.
"""

from django.db import models
from core.models import Staff, Student

class StaffAttendance(models.Model):
    """Model for attendance records of staff."""

    class Status(models.TextChoices):
        PRESENT = 'Present'
        ABSENT = 'Absent'

    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PRESENT)
    comment = models.CharField(max_length=20, blank=True)

    class Meta:
        unique_together = ('staff', 'date')

class StudentAttendance(models.Model):
    """Model for attendance records of students."""

    class Status(models.TextChoices):
        PRESENT = 'Present'
        ABSENT = 'Absent'

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PRESENT)
    comment = models.CharField(max_length=20, blank=True)

    class Meta:
        unique_together = ('student', 'date')

