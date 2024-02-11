from django.views.generic import CreateView
from django.contrib.auth import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from users.forms import LoginUserForm, RegisterUserForm, ChangePasswordForm


class LoginUser(views.LoginView):
    """Displays the login form and handle the logins action"""

    form_class = LoginUserForm
    template_name = "users/login.html"
    extra_context = {"title": "Авторизация"}


class RegisterUser(CreateView):
    """View for registration a new user, with a response rendered by a template"""

    form_class = RegisterUserForm
    template_name = "users/registration.html"
    extra_context = {"title": "Регистрация"}
    success_url = reverse_lazy("users:login")


class ChangePassword(LoginRequiredMixin, views.PasswordChangeView):
    """Displays the password change form and navigates to the next page"""

    form_class = ChangePasswordForm
    template_name = "users/change_password.html"
    success_url = reverse_lazy("users:done_change")
    extra_context = {"title": "Смена пароля"}


class ChangePasswordDone(views.PasswordChangeDoneView):
    """Displays the password change done and navigates to the next page"""

    template_name = "users/change_password_done.html"


class PasswordResetViewUser(views.PasswordResetView):
    """Displays the password reset form and navigates to the next page"""

    template_name = "users/password_reset_form.html"
    email_template_name = "users/password_reset_email.html"
    success_url = reverse_lazy("users:password_reset_done")


class PasswortResetDoneViewUser(views.PasswordChangeDoneView):
    """Displays the password reset done and navigates to the next page"""

    template_name = "users/password_reset_done.html"


class PasswordResetConfirmViewUser(views.PasswordResetConfirmView):
    """Displays the password reset confirm and navigates to the next page"""

    template_name = "users/password_reset_confirm.html"
    success_url = reverse_lazy("users:password_reset_complete")


class PasswordResetCompleteViewUser(views.PasswordResetCompleteView):
    """Displays the password reset complete and navigates to the next page"""

    template_name = "users/password_reset_complete.html"
