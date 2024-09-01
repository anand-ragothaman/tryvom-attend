from django.db import models

from app.models.member_models import Member

class Attendance(models.Model):
    class Status(models.IntegerChoices):
        PRESENT = 1, 'Present'
        ABSENT = 2, 'Absent'
        HOLIDAY = 0, 'Holiday'
        
    member = models.ForeignKey(
        Member, on_delete=models.CASCADE)
    status = models.IntegerField(choices=Status.choices, default=Status.HOLIDAY)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.member} {self.get_status_display()} {self.date}"