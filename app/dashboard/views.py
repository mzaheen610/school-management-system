"""
Views for the dashboards.
"""

from django.shortcuts import render
from attendance.models import StudentAttendance
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def dashboardView(request):
    """Sample dashboard view."""
    # studentID = request.query_params.get('student-id')
    attendance = StudentAttendance.objects.filter(student='S005').order_by('date').all()
    absent_count = 0
    dates = []
    data = []
    for item in attendance:
        dates.append(item.date)
        if item.status == "Present":
            data.append(1)
        else:
            data.append(0)
            absent_count += 1
    return render(request, 'sample.html', {'attendance_data' : attendance[0], 'dates': dates, 'data': data, 'absent_count': absent_count})


@api_view(['POST'])
def attendanceDataView(request):
    """View to get attendance data of a particular student."""
    if request.method == "POST" and 'student_id' in request.data:

        if not type(request.data['student_id']) == str:
            return Response({'error': "student_id must be a string"}, status=400)

        studentID = request.data['student_id']
        # print(studentID)
        # print(type(studentID))
        attendance = StudentAttendance.objects.filter(student=studentID).order_by('date').all()
        if not attendance:
            return Response({'error': "Student with the given id does not exist."})
        # print(attendance)
        absent_count = 0
        dates = []
        data = []
        for item in attendance:
            dates.append(item.date)
            if item.status == "Present":
                data.append(1)
            else:
                data.append(0)
                absent_count += 1
        # print(type(attendance[0].student.name))
        return Response({'student': attendance[0].student.name, 'dates': dates, 'data': data, 'absent_count': absent_count})
    return Response({'error': 'Missing student_id in request data'}, status=400)
