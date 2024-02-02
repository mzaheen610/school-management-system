"""
Urls for user login and logout.
"""
from django.urls import path
from classrooms import views

urlpatterns = [
    path("list-teacher/", views.ListTeacherView.as_view(), name="list-teacher"),
    path("create-teacher/", views.CreateTeacherView.as_view(), name="create-teacher"),
    path("update-teacher/<int:teacher_id>/", views.UpdateTeacherView.as_view(), name="update-teacher"),
    path("delete-teacher/<int:teacher_id>/", views.DeleteTeacherView.as_view(), name="delete-teacher")
] + [
    path("list-subject/", views.ListSubjectView.as_view(), name="list-subject"),
    path("create-subject/", views.CreateSubjectView.as_view(), name="create-subject"),
    path("update-subject/<int:subject_id>/", views.updateSubjectView.as_view(), name="update-subject"),
    path("delete-subject/<int:subject_id>/", views.DeleteSubjectView.as_view(), name="delete-subject")
] + [
    path("list-Class/", views.ListClassView.as_view(), name="list-Class"),
    path("create-Class/", views.CreateClassView.as_view(), name="create-Class"),
    path("update-Class/<int:Class_id>/", views.updateClassView.as_view(), name="update-Class"),
    path("delete-Class/<int:Class_id>/", views.DeleteClassView.as_view(), name="delete-Class")
] + [
    path("list-ClassSchedule/", views.ListClassSchedulesView.as_view(), name="list-ClassSchedule"),
    path("create-ClassSchedule/", views.CreateClassSchedulesView.as_view(), name="create-ClassSchedule"),
    path("update-ClassSchedule/<int:schedule_id>/", views.UpdateClassSchedulesView.as_view(), name="update-ClassSchedule"),
    path("delete-ClassSchedule/<int:schedule_id>/", views.DeleteClassSchedulesView.as_view(), name="delete-ClassSchedule")
] + [
    path("create-day-schedule", views.CreateDayScheduleView.as_view(), name="create-day-schedule")
]