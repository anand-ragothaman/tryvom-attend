from django.http import HttpResponse
from django.shortcuts import redirect, render

from app.forms.category_forms import Category_add_form
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
