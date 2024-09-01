from django.urls import path

from app.views import report_views


urlpatterns = [
    path('', report_views.report, name="report")
]
