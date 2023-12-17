# -*- coding: utf-8 -*- 
from django import forms
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField
class UserForm(forms.Form):
    Identify = (
        ('0', "读者"),
        ('1', "作者"),
    )
    user_role=forms.ChoiceField(label='身份:', choices=Identify)
    userID = forms.CharField(label='账号:', max_length=16, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码:", max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
class RegisterForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    Identify = (
        ('0', "读者"),
        ('1', "作者"),
    )
    user_role = forms.ChoiceField(label='身份:', choices=Identify)
    username = forms.CharField(label="用户名:", max_length=16, widget=forms.TextInput(attrs={'class': 'form-control'}))
    nickname = forms.CharField(label="姓名:", max_length=16, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码:", max_length=16,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码:", max_length=16,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    phone=forms.CharField(label="手机号",min_length=11, max_length=11,widget=forms.TextInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性别:', choices=gender)

