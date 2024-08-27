from django.urls import path, include
from app.views import category_views

urlpatterns = [
    path('', category_views.category, name='category'),
    path('category-add-submit', category_views.category_add_submit,
         name='category.category_add_submit'),
]
