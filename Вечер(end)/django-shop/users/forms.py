from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    """Эта форма предоставляет поля для заполнения, такие как имя пользователя, электронная почта и пароль."""
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    """Эта форма предоставляет поля для заполнения, такие как имя пользователя и пароль."""
    class Meta:
        model = User
        fields = ('username', 'password')
