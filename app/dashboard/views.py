"""
Views for the dashboards.
"""

from django.shortcuts import render
from attendance.models import StudentAttendance
from rest_framework.views import APIView
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

