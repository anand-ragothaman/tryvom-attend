from django.http import HttpResponse
from django.shortcuts import redirect, render

from app.forms.member_form import Member_add_form, Member_edit_form
from app.models.attendance_models import Attendance
from app.models.category_models import Category
from app.models.member_models import Member
from app.views.menus import menus
from django.contrib import messages
from datetime import date, datetime


def attendance(request):
    form = Member_add_form()
    categories = Category.objects.all()
    
    cat = request.GET.get('cat')
    
    if cat == '0':
        members = Member.objects.filter(category=None).order_by('name')
        print(members)
    elif cat is None:
        members = Member.objects.all().order_by('name')
    elif cat is not None:
        cat = int(cat)
        members = Member.objects.filter(category=cat).order_by('name')
    
    data = {
        'menus': menus,
        'categories' : categories,
        'members': members,
        'cat':cat,
        'today_date' : date.today()
    }
    return render(request, 'attendance/attendance.html', data)

def attendance_submit(request):
    if request.method == 'POST':
        cat = request.POST.get('cat')
       
        if cat == '0':
            members = Member.objects.filter(category=None).order_by('name')
        elif cat is None:
            members = Member.objects.all().order_by('name')
        elif cat is not None:
            cat = int(cat)
            members = Member.objects.filter(category=cat).order_by('name')
     
        for member in members:
            if str(member.id) in request.POST.keys():
                attendance_status = 1
            else:
                attendance_status = 2
            exists = Attendance.objects.filter(member=member,date=date.today()).exists()
            
            if not exists:
                attendance = Attendance(
                    member=member,
                    status = attendance_status,
                    date = date.today()
                )
                attendance.save()
            else:
                attendance = Attendance.objects.filter(member=member,date=date.today()).first()
                attendance.status = attendance_status
                attendance.save()
            
        messages.add_message(
            request,
            messages.SUCCESS,
            "Attendance submitted to respective Members successfully!"
        )
        return redirect(request.META.get('HTTP_REFERER', 'default_redirect_url'))
    else:
        messages.add_message(request, messages.WARNING, "Something Wrong!")
        return redirect(request.META.get('HTTP_REFERER', 'default_redirect_url'))