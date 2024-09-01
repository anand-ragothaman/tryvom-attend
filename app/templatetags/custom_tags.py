from datetime import datetime
from django import template
from app.models.attendance_models import Attendance

register = template.Library()


@register.simple_tag
def get_member_attendance_status(member,date):
    exists = Attendance.objects.filter(member=member,date=date).exists()
    if not exists:
        return 0
    else:
        return Attendance.objects.filter(member=member,date=date).first().status

@register.simple_tag
def get_member_attendance_counts(member,from_date,to_date):
    no_of_days=0
    present=0
    absent=0
    not_taken=0
    
    start_date = datetime.strptime(from_date, '%Y-%m-%d').date()
    end_date = datetime.strptime(to_date, '%Y-%m-%d').date()
    no_of_days=(end_date - start_date).days
    present = Attendance.objects.filter(member=member,date__range=(start_date, end_date),status=1).count()
    absent = Attendance.objects.filter(member=member,date__range=(start_date, end_date),status=2).count()
    not_taken = (end_date - start_date).days-(present+absent)
    
    return {
        'no_of_days':no_of_days,
        'present':present,
        'absent':absent,
        'not_taken':not_taken,
    }

@register.filter  
def string_to_date(value, date_format='%Y-%m-%d'):
    try:
        # Convert the string to a datetime object
        date_obj = datetime.strptime(value, '%d-%m-%Y')
        # Format the datetime object as a string
        return date_obj.strftime(date_format)
    except ValueError:
        return "Invalid date format"