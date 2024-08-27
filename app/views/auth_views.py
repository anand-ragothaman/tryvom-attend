from django.contrib.auth import login, authenticate, logout
from app.forms.forms import LoginForm
from django.contrib import messages
from django.shortcuts import render, redirect


def login_view(request):
    if 'next' in request.GET:
        next_route = request.GET['next']
    else:
        next_route = None

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if next_route != None:
                    return redirect(next_route)
                else:
                    return redirect('dashboard')  # Redirect to a success page.
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()

    data = {
        'form': form,
        'next_route': next_route
    }

    return render(request, 'auth/login.html', data)


def logout_view(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "Logged out successfully!")
    return redirect('/')
