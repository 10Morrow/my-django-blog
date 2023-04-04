from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')


class RegistrationUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'password_confirm')

    def clean(self):
        cleaned_data = super(RegistrationUserForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('password_confirm')
        if password and confirm_password and confirm_password != password:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data
