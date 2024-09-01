
from django.urls import path, include
from app.views import auth_views, views
from app.urls import attendance_urls, category_urls, member_urls, report_urls, user_urls

urlpatterns = [
    path('', auth_views.login_view, name='auth.login'),
    path('auth/logout/', auth_views.logout_view, name='auth.logout'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('category/', include(category_urls)),
    path('members/', include(member_urls)),
    path('attendance/', include(attendance_urls)),
    path('report/', include(report_urls)),
    path('users/', include(user_urls)),


]
