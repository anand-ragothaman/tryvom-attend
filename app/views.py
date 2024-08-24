from django.shortcuts import render
from django.http import HttpResponse

class Auth:
    def login(request):
        return render(request, 'auth/login.html')
