from django.http import HttpResponse
from django.shortcuts import redirect, render

from app.forms.member_form import Member_add_form, Member_edit_form
from app.forms.user_forms import User_add_form
from app.models.category_models import Category
from app.models.member_models import Member
from app.views.menus import menus
from django.contrib import messages


def users(request):
    form = User_add_form()
    # form.fields['category'].queryset = Category.objects.all()
    members = Member.objects.all().order_by('name')

    data = {
        'menus': menus,
        'form': form,
        'members': members
    }
    return render(request, 'users/users.html', data)