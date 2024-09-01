from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
    class Types(models.IntegerChoices):
        ADMIN = 1, 'Admin'
        ATTENDANCE_TAKER = 2, 'Attendance Taker'
        
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    type = models.IntegerField(choices=Types.choices, default=Types.ATTENDANCE_TAKER)
    categories = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"{self.user} {self.type}"