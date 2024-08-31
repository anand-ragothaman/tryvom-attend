from django.urls import path, include

from app.views import member_views

urlpatterns = [
    path('', member_views.members, name='members'),
    path('add-member-submit', member_views.add_member_submit,
         name='members.add_member_submit'),
    path('edit-member/<int:member_id>/', member_views.edit_member,
         name='members.edit_member'),
    path('edit-member-submit', member_views.edit_member_submit,
         name='members.edit_member_submit'),
    path('view-member-description/<int:member_id>/', member_views.view_member_description,
         name='members.view_member_description'),
    path('delete-member-submit', member_views.delete_member_submit,
         name='members.delete_member_submit'),
]
