from datetime import date
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse

from app.forms.user_forms import Change_password_form, My_profile_form
from app.models.attendance_models import Attendance
from app.models.category_models import Category
from app.models.member_models import Member
from app.views.menus import menus
from django.contrib import messages
from django.contrib.auth.models import User


def dashboard(request):
    total_members = Member.objects.count()
    total_categories = Category.objects.count()
    total_presents = Attendance.objects.filter(
        status=1,
        date=date.today()
    ).count()
    total_absents = Attendance.objects.filter(
        status=2,
        date=date.today()
    ).count()
    not_takens = total_members-(total_presents+total_absents)
    data = {
        'menus': menus,
        'total_members': total_members,
        'total_categories': total_categories,
        'total_presents': total_presents,
        'total_absents': total_absents,
        'not_takens': not_takens
    }
    return render(request, 'dashboard.html', data)


def my_profile(request):
    profile_form = My_profile_form(
        initial={
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'username': request.user.username,
            'email': request.user.email,
        }
    )
    change_password_form = Change_password_form(user=request.user)
    if request.method == 'POST':
        form = My_profile_form(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            user = User.objects.filter().first()
            user.first_name = form_data['first_name']
            user.last_name = form_data['last_name']
            user.username = form_data['username']
            user.email = form_data['email']
            user.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Profile updated successfully!"
            )
            return redirect(request.META.get('HTTP_REFERER', 'default_redirect_url'))
    data = {
        'menus': menus,
        'profile_form': profile_form,
        'change_password_form': change_password_form
    }
    return render(request, 'my-profile.html', data)


def change_password_submit(request):
    profile_form = My_profile_form(
        initial={
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'username': request.user.username,
            'email': request.user.email,
        }
    )
    if request.method == 'POST':
        change_password_form = Change_password_form(
            user=request.user, data=request.POST)
        if change_password_form.is_valid():
            user = change_password_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Password updated successfully!"
            )
            return redirect('auth.login')
        else:
            print(change_password_form.errors)
            messages.add_message(request, messages.WARNING, "Something Wrong!")
            return render(request, 'my-profile.html', {'menus': menus, 'profile_form': profile_form, 'change_password_form': change_password_form})
    else:
        messages.add_message(request, messages.WARNING, "Something Wrong!")
        return redirect(request.META.get('HTTP_REFERER', 'default_redirect_url'))
