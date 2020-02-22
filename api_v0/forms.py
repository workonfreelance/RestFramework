from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

# class LoginForm(ModelForm):
#     class Meta:
#         model = Form
#         fields = ['login', 'Email', 'file']




#
# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['FirsName', 'LastName', 'text']


# class CommentForm(forms.Form):
#     comment = forms.CharField(label='Your comment', max_length=100)
#
#
# class UserRegistrationForm(forms.ModelForm):
#     username = forms.CharField(label='Your name', max_length=100)
#     password = forms.CharField(label='Password',
#                                widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Repeat password',
#                                 widget=forms.PasswordInput)
#
#
#     class Meta:
#         model = User
#         fields =  ('username','email','password','password2')
#
#
#     def clean_password2(self):
#         cd = self.cleaned_data
#
#         if cd['password'] != cd['password2']:
#             raise forms.ValidationError('Passwords don\'t match.')
#         return cd['password2']
#
# class UserLoginForm(forms.ModelForm):
#     username = forms.CharField(label='Your name', max_length=100)
#     password = forms.CharField(label='Password',
#                                widget=forms.PasswordInput)
#
#
