from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse

from app.views.menus import menus


def dashboard(request):
    data = {
        'menus': menus
    }
    return render(request, 'dashboard.html', data)
