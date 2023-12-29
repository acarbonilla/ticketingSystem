
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('baseApp.urls')),
    path('accounts/', include('allauth.urls')),
    path('home/', TemplateView.as_view(template_name='forms/login.html'), name='home'),
    path('admin/', admin.site.urls),
    path('record/', include('staff.urls')),
    path('deskside/', include('deskside.urls')),
    path('member/', include('member.urls')),
    path('api/', include('ticketingAPI.urls')),
    path('api-auth/', include('rest_framework.urls')),
    # This is for password reset
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
