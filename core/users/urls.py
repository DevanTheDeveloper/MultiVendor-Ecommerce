from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from users import views as user_views


urlpatterns = [

    path('register/', user_views.register, name='cx_register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='cx_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='cx_logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html',
    ) ,name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html',
    ), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
        name= 'password_reset_complete'),

    ]