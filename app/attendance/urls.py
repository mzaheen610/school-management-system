"""
Urls for the attendance API.
"""

from django.urls import path, include
from .views import StudentAttendanceView, StudentAttendancePageView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('student-attendance', StudentAttendanceView)

app_name = 'attendance'

urlpatterns = [
    path('api/', include(router.urls), name='attendance'),
    path('attendance/student', StudentAttendancePageView, name='mark-attendance' )
]