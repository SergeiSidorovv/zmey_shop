from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordChangeForm,
)
from django.contrib.auth import get_user_model
from django import forms
from captcha.fields import CaptchaField


class LoginUserForm(AuthenticationForm):
    """User login form"""

    username = forms.CharField(label="Логин", widget=forms.TextInput())
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput())
    captcha = CaptchaField()

    class Meta:
        """Metadata by form"""

        model = get_user_model()
        fields = ["username", "password"]


class RegisterUserForm(UserCreationForm):
    """User registration form"""

    username = forms.CharField(label="Логин", widget=forms.TextInput())
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput())
    captcha = CaptchaField()

    class Meta:
        """Metadata by form"""

        model = get_user_model()
        fields = ["username", "password1", "password2", "email"]
        labels = {"email": "E-mail"}
        widgets = {"email": forms.TextInput()}

    def clean_email(self):
        """Checks for a similar email address"""

        email = self.cleaned_data["email"]
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже используется!")
        return email


class ChangePasswordForm(PasswordChangeForm):
    """User change password form"""

    old_password = forms.CharField(label="Пароль", widget=forms.PasswordInput())
    new_password1 = forms.CharField(label="Новый пароль", widget=forms.PasswordInput())
    new_password2 = forms.CharField(
        label="Повторить новый  пароль", widget=forms.PasswordInput()
    )
    captcha = CaptchaField()
