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
]