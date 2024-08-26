
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login_view, name='auth.login'),
    path('auth/logout/', views.logout_view, name='auth.logout'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('users/all-users', views.dashboard, name='users.all_users'),
    path('users/all-users', views.dashboard, name='users.add_user'),
]
