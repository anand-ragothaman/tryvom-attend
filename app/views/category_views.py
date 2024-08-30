from django.http import HttpResponse
from django.shortcuts import redirect, render

from app.forms.category_forms import Category_add_form, Category_edit_form
from app.models.category_models import Category
from app.views.menus import menus
from django.contrib import messages


def category(request):
    form = Category_add_form
    categories = Category.objects.all()
    data = {
        'menus': menus,
        'form': form,
        'categories': categories
    }
    return render(request, 'category/category.html', data)


def category_add_submit(request):
    if request.method == 'POST':
        form = Category_add_form(request.POST)
        if form.is_valid():
            category_name = form.cleaned_data.get('category')
            category = Category(
                category=category_name
            )
            category.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Category added successfully!"
            )
    else:
        messages.add_message(request, messages.WARNING, "Something Wrong!")

    return redirect(request.META.get('HTTP_REFERER', 'default_redirect_url'))


def category_edit(request, category_id):
    edit_category = Category.objects.get(id=category_id)

    form = Category_edit_form(
        initial={
            'id': edit_category.id,
            'category': edit_category.category
        }
    )
    data = {
        'menus': menus,
        'form': form,
        'edit_category': edit_category
    }
    return render(request, 'category/category-edit.html', data)


def category_edit_submit(request):
    if request.method == 'POST':
        form = Category_edit_form(request.POST)
        if form.is_valid():
            category_name = form.cleaned_data.get('category')
            category_id = form.cleaned_data.get('id')
            category = Category.objects.get(id=category_id)
            category.category = category_name
            category.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Category updated successfully!"
            )
            return redirect('category')
    else:
        messages.add_message(request, messages.WARNING, "Something Wrong!")
        return redirect(request.META.get('HTTP_REFERER', 'default_redirect_url'))


def category_delete_submit(request):
    if request.method == 'POST':
        try:
            delete_id = request.POST.get('id')
        except:
            messages.add_message(request, messages.WARNING, "Invalid id")
            return redirect(request.META.get('HTTP_REFERER', 'default_redirect_url'))

        Category.objects.get(id=delete_id).delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            "Category deleted successfully!"
        )
        return redirect('category')
    else:
        messages.add_message(request, messages.WARNING, "Something Wrong!")
        return redirect(request.META.get('HTTP_REFERER', 'default_redirect_url'))
