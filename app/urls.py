from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Auth.login, name='auth.login'),

    path('dashboard/', views.dashboard, name='dashboard'),
]
