from django.http import HttpResponse
from django.shortcuts import redirect, render

from app.forms.member_form import Member_add_form, Member_edit_form
from app.models.category_models import Category
from app.models.member_models import Member
from app.views.menus import menus
from django.contrib import messages


def members(request):
    form = Member_add_form()
    # form.fields['category'].queryset = Category.objects.all()
    members = Member.objects.all().order_by('name')

    data = {
        'menus': menus,
        'form': form,
        'members': members
    }
    return render(request, 'members/members.html', data)


def add_member_submit(request):
    if request.method == 'POST':
        form = Member_add_form(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            member = Member(**form_data)
            member.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Member added successfully!"
            )
        else:
            print(form.errors)
    else:
        messages.add_message(request, messages.WARNING, "Something Wrong!")

    return redirect(request.META.get('HTTP_REFERER', 'default_redirect_url'))


def edit_member(request, member_id):
    edit_member = Member.objects.get(id=member_id)

    form = Member_edit_form(
        initial={
            'id': edit_member.id,
            'name': edit_member.name,
            'member_id': edit_member.member_id,
            'description': edit_member.description,
            'category': edit_member.category
        }
    )
    data = {
        'menus': menus,
        'form': form,
        'edit_member': edit_member
    }
    return render(request, 'members/edit-member.html', data)


def edit_member_submit(request):
    if request.method == 'POST':
        form = Member_edit_form(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            edit_member = Member.objects.get(id=form_data['id'])
            edit_member.name = form_data['name']
            edit_member.member_id = form_data['member_id']
            edit_member.description = form_data['description']
            edit_member.category = form_data['category']
            edit_member.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Member updated successfully!"
            )
            return redirect('members')
        else:
            print(form.errors)
            messages.add_message(request, messages.WARNING, "Something Wrong!")
            return redirect(request.META.get('HTTP_REFERER', 'default_redirect_url'))
    else:
        messages.add_message(request, messages.WARNING, "Something Wrong!")
        return redirect(request.META.get('HTTP_REFERER', 'default_redirect_url'))


def view_member_description(request, member_id):
    member = Member.objects.get(id=member_id)

    data = {
        'menus': menus,
        'member': member
    }
    return render(request, 'members/member-description.html', data)


def delete_member_submit(request):
    if request.method == 'POST':
        try:
            delete_id = request.POST.get('id')
        except:
            messages.add_message(request, messages.WARNING, "Invalid id")
            return redirect(request.META.get('HTTP_REFERER', 'default_redirect_url'))

        Member.objects.get(id=delete_id).delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            "Member deleted successfully!"
        )
        return redirect('members')
    else:
        messages.add_message(request, messages.WARNING, "Something Wrong!")
        return redirect(request.META.get('HTTP_REFERER', 'default_redirect_url'))
