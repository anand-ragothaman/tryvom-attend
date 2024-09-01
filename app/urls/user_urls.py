from django.urls import path

from app.views import user_views


urlpatterns = [
    path('',user_views.users,name="users")
]
