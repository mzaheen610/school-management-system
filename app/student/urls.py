"""
Urls for the student API.
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()
router.register('student', views.StudentAPIView)

app_name = 'student'

urlpatterns = [
    path('api/', include(router.urls), name='student'),
    path('student/enroll', views.StudentEnrollmentPageView, name = 'student_enrollment_page'),
    path('student/profile', views.StudentProfileView, name = 'student_profile'),
]
