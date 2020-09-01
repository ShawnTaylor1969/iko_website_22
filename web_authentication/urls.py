from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'web_authentication'

urlpatterns = [
    path('passwordchanged/', views.PasswordChangedView.as_view(), name="password_changed"),
    path('changepassword/', auth_views.PasswordChangeView.as_view(
        template_name='web_authentication/change_password.html',
        success_url='/authentication/passwordchanged'), name='change_password'),

    path('password_reset/',
        auth_views.PasswordResetView.as_view(
            template_name='web_authentication/password_reset.html',
            subject_template_name='web_authentication/password_reset_subject.txt',
            email_template_name='web_authentication/password_reset_email.html',
        ), name = 'password_reset'),
    path('password_reset_done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='web_authentication/password_reset_done.html',
        ), name = 'password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='web_authentication/password_reset_confirm.html',
        ), name = 'password_reset_confirm'),
    path('password_reset_complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='web_authentication/password_reset_complete.html',
        ), name = 'password_reset_complete'),
]
