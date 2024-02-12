from django.contrib.auth.forms import AuthenticationForm
from django import forms
from captcha.fields import CaptchaField

class LoginAdminUserForm(AuthenticationForm):
    """User admin login formm"""

    username = forms.CharField(label="Логин", widget=forms.TextInput())
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput())
    captcha = CaptchaField()