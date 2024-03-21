from django.urls import path
from .views import login_view, AboutMeView, logout_view, RegisterView, edit_user, edit_password
from django.contrib.auth.views import (LogoutView,
                                       PasswordResetView,
                                       PasswordResetDoneView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       )


app_name = 'myauth'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('user_page/', AboutMeView.as_view(), name='user_page'),
    # path('images/', edit_password, name='password_change'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('edit_user_info/', edit_user, name='edit_user'),
    path('password_change/', edit_password, name='password_change'),
    path('password_reset/', PasswordResetDoneView.as_view(
        template_name='myauth/password_reset.html'),
         name='password_reset'),
    path('password_reset/done/', PasswordResetView.as_view(
        template_name='myauth/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='myauth/password_reset_confirm.html'),
         name='password_reset_confirm'),
]

