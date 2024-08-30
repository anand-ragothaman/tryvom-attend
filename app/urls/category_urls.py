from django.urls import path, include
from app.views import category_views

urlpatterns = [
    path('', category_views.category, name='category'),
    path('category-add-submit', category_views.category_add_submit,
         name='category.category_add_submit'),
    path('category-edit/<int:category_id>/', category_views.category_edit,
         name='category.category_edit'),
    path('category-edit-submit', category_views.category_edit_submit,
         name='category.category_edit_submit'),
    path('category-delete-submit', category_views.category_delete_submit,
         name='category.category_delete_submit'),
]
