# -*- coding:utf-8 -*- 
__author__ = 'jiangjun'
__date__ = '2018/3/14 16:58 '

from django import forms
from captcha.fields import CaptchaField


class RegisterForm(forms.Form):
    username = forms.CharField(required=True, min_length=4)
    email = forms.CharField(required=True, min_length=12)
    password1 = forms.CharField(required=True, min_length=6)
    password2 = forms.CharField(required=True, min_length=6)
    captcha = CaptchaField(error_messages={'invalid': '验证码错误'})


class LoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=4)
    password = forms.CharField(required=True, min_length=6)
