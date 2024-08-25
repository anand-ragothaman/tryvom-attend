from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse

from app.forms import LoginForm


class Auth:
    def login(request):
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('dashboard')  # Redirect to a success page.
                else:
                    form.add_error(None, "Invalid username or password")
        else:
            form = LoginForm()
        return render(request, 'auth/login.html', {'form': form})

def dashboard(request):
    return render(request, 'dashboard.html')