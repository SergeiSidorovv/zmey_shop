from django.urls import path
from django.contrib.auth.views import LogoutView

from users import views


app_name = "users"

urlpatterns = [
    path("login/", views.LoginUser.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("registration/", views.RegisterUser.as_view(), name="registration"),
    path("change_password/", views.ChangePassword.as_view(), name="change"),
    path(
        "change_password_done/",
        views.ChangePasswordDone.as_view(),
        name="done_change",
    ),
    path(
        "password-reset/", views.PasswordResetViewUser.as_view(), name="password_reset"
    ),
    path(
        "password-reset/done/",
        views.PasswortResetDoneViewUser.as_view(),
        name="password_reset_done",
    ),
    path(
        "password-reset/<uidb64>/<token>/",
        views.PasswordResetConfirmViewUser.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password_reset_complete",
        views.PasswordResetCompleteViewUser.as_view(),
        name="password_reset_complete",
    ),
]
