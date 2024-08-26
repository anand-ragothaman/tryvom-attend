from django.urls import path, include
from app.views import category_views

urlpatterns = [
    path('', category_views.category, name='category'),
]
