from django.urls import path

from app.views import attendance_views


urlpatterns = [
    path('',attendance_views.attendance, name="attendance.attendance"),
    path('attendance-submit',attendance_views.attendance_submit, name="attendance.attendance_submit")
]
