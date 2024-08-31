
from django.urls import path, include
from app.views import auth_views, views
from app.urls import category_urls, member_urls

urlpatterns = [
    path('', auth_views.login_view, name='auth.login'),
    path('auth/logout/', auth_views.logout_view, name='auth.logout'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('category/', include(category_urls)),
    path('members/', include(member_urls)),


]
