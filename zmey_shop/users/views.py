from django.views.generic import CreateView
from django.contrib.auth import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from users.forms import LoginUserForm, RegisterUserForm, ChangePasswordForm


class LoginUser(views.LoginView):
    form_class = LoginUserForm
    template_name = "users/login.html"
    extra_context = {"title": "Авторизация"}


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "users/registration.html"
    extra_context = {"title": "Регистрация"}
    success_url = reverse_lazy("users:login")


class ChangePassword(LoginRequiredMixin, views.PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = "users/change_password.html"
    success_url = reverse_lazy("users:done_change")
    extra_context = {"title": "Смена пароля"}


class ChangePasswordDone(views.PasswordChangeDoneView):
    template_name = "users/change_password_done.html"


class PasswordResetViewUser(views.PasswordResetView):
    template_name = "users/password_reset_form.html"
    email_template_name = "users/password_reset_email.html"
    success_url = reverse_lazy("users:password_reset_done")


class PasswortResetDoneViewUser(views.PasswordChangeDoneView):
    template_name = "users/password_reset_done.html"


class PasswordResetConfirmViewUser(views.PasswordResetConfirmView):
    template_name = "users/password_reset_confirm.html"
    success_url = reverse_lazy("users:password_reset_complete")


class PasswordResetCompleteViewUser(views.PasswordResetCompleteView):
    template_name = "users/password_reset_complete.html"
