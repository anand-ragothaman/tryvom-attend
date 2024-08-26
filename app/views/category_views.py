from django.http import HttpResponse
from django.shortcuts import render

from app.views.menus import menus


def category(request):
    data = {
        'menus': menus
    }
    return render(request, 'category/category.html', data)
