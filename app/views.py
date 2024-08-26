from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from app.decorators import unauthenticated_user
from app.forms import LoginForm


@unauthenticated_user
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

@login_required
def dashboard(request):
    menus = [
            {
                'name': 'Dashboard',
                'icon':'d',
                'route':'dashboard',
                'type': 0
            },
         {
              'name': 'Users',
              'icon':'u',
              'type': 1,
              'sub_menus':[
                {
                    'name': 'All Users',
                    'route':'users.all_users',
                },{
                    'name': 'Add User',
                    'route':'users.add_user',
                }
            ]
                
         } 
            
    ]
    
    
    
    data={
        'menus':menus
    }
    return render(request, 'dashboard.html', data)
