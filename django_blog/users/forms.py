from django.core.exceptions import ValidationError
import re

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')


def validate_latin_characters(username):
    pattern = re.compile('[^a-zA-Z]')
    if pattern.search(username):
        raise ValidationError('Поле username может содержать лишь буквы латиницы')

def validate_letters(value):
    pattern = re.compile('[^a-zA-Zа-яА-Я]')
    if pattern.search(value):
        raise ValidationError('Поле может содержать только буквы')

class RegistrationUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    first_name = forms.CharField(validators=[validate_letters])
    last_name = forms.CharField(validators=[validate_letters])
    username = forms.CharField(validators=[validate_latin_characters])
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'password_confirm')

    def clean_password_confirm(self):
        cleaned_data = super(RegistrationUserForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('password_confirm')
        if len(password)<5:
            raise forms.ValidationError("Длинна пароля не может быть меньше 5 символов")
        if password and confirm_password and confirm_password != password:
            raise forms.ValidationError("пароли не совпадают")
        return cleaned_data


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label='пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))

