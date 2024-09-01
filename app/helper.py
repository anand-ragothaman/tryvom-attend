from app.models.attendance_models import Attendance


def get_member_attendance_status(member,date):
    exists = Attendance.objects.filter(member=member,date=date).exists()
    if not exists:
        return 0
    else:
        return Attendance.objects.filter(member=member,date=date).first().status