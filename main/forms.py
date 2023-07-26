from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.hashers import make_password

from .models import User


# class SignUpForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('image', 'first_name', 'last_name', 'email', 'company')


# class EditForm():
#     class Meta:
#         model = User
#         fields = ['image', 'first_name', 'last_name', 'email', 'company']
#
#     def clean_password(self):
#         return make_password(self.cleaned_data['password'])
